"""
Tests unitaires pour l'application IAMonJob
"""

import pytest
import json
import os
from app import app as flask_app


@pytest.fixture
def app():
    """Fixture Flask app pour les tests"""
    flask_app.config['TESTING'] = True
    flask_app.config['UPLOAD_FOLDER'] = 'test_uploads'
    yield flask_app
    
    # Cleanup
    if os.path.exists('test_uploads'):
        import shutil
        shutil.rmtree('test_uploads')


@pytest.fixture
def client(app):
    """Fixture client de test"""
    return app.test_client()


class TestHealthEndpoint:
    """Tests pour l'endpoint /api/health"""
    
    def test_health_check(self, client):
        """Test que l'endpoint health retourne OK"""
        response = client.get('/api/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'ok'
        assert 'timestamp' in data


class TestModulesEndpoint:
    """Tests pour l'endpoint /api/modules"""
    
    def test_get_modules(self, client):
        """Test que l'endpoint modules retourne la liste complète"""
        response = client.get('/api/modules')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'cv_only' in data
        assert 'cv_and_offer' in data
        
        # Vérifie qu'il y a 4 modules CV seul
        assert len(data['cv_only']) == 4
        
        # Vérifie qu'il y a 7 modules CV + offre
        assert len(data['cv_and_offer']) == 7
        
        # Vérifie la structure d'un module
        first_module = data['cv_only'][0]
        assert 'id' in first_module
        assert 'name' in first_module
        assert 'description' in first_module


class TestAnalyzeEndpoint:
    """Tests pour l'endpoint /api/analyze"""
    
    def test_analyze_missing_api_key(self, client):
        """Test que la requête sans API key échoue"""
        response = client.post('/api/analyze', data={})
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert 'error' in data
        assert 'API key' in data['error']
    
    def test_analyze_missing_cv(self, client):
        """Test que la requête sans CV échoue"""
        response = client.post('/api/analyze', data={
            'api_key': 'test-key'
        })
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert 'error' in data
        assert 'CV' in data['error']
    
    def test_analyze_invalid_file_type(self, client):
        """Test que les types de fichiers invalides sont rejetés"""
        from io import BytesIO
        
        response = client.post('/api/analyze', data={
            'api_key': 'test-key',
            'cv': (BytesIO(b'fake content'), 'test.exe')
        })
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert 'error' in data


class TestFileUploadValidation:
    """Tests pour la validation des fichiers"""
    
    def test_allowed_file_extensions(self):
        """Test que les extensions autorisées sont correctes"""
        from app import allowed_file
        
        assert allowed_file('cv.pdf') is True
        assert allowed_file('cv.docx') is True
        assert allowed_file('cv.doc') is True
        assert allowed_file('cv.txt') is True
        assert allowed_file('cv.png') is True
        assert allowed_file('cv.jpg') is True
        assert allowed_file('cv.jpeg') is True
        
        assert allowed_file('cv.exe') is False
        assert allowed_file('cv.sh') is False
        assert allowed_file('cv') is False
        assert allowed_file('cv.') is False


class TestMediaTypeDetection:
    """Tests pour la détection du type MIME"""
    
    def test_get_media_type(self):
        """Test que les types MIME sont correctement détectés"""
        from app import get_media_type
        
        assert get_media_type('file.pdf') == 'application/pdf'
        assert get_media_type('file.docx') == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        assert get_media_type('file.png') == 'image/png'
        assert get_media_type('file.jpg') == 'image/jpeg'
        assert get_media_type('file.jpeg') == 'image/jpeg'
        assert get_media_type('file.txt') == 'text/plain'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
