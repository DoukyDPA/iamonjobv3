#!/usr/bin/env python3
"""
IAMonJob Web Application Backend
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime
import base64
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc', 'txt', 'png', 'jpg', 'jpeg'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def file_to_base64(filepath):
    with open(filepath, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def get_media_type(filename):
    ext = filename.rsplit('.', 1)[1].lower()
    media_types = {
        'pdf': 'application/pdf',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'doc': 'application/msword',
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'txt': 'text/plain'
    }
    return media_types.get(ext, 'application/octet-stream')

# API ROUTES EN PREMIER
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'timestamp': datetime.now().isoformat()})

@app.route('/api/modules', methods=['GET'])
def get_modules():
    modules = {
        'cv_only': [
            {'id': 1, 'name': 'Analyse du CV', 'description': 'Analyse complète avec forces et faiblesses'},
            {'id': 2, 'name': 'Tableau des compétences', 'description': 'Matrices hard skills et soft skills'},
            {'id': 3, 'name': 'Notation et améliorations', 'description': 'Note /10 et plan d\'amélioration'},
            {'id': 4, 'name': 'Évolutions professionnelles', 'description': 'Pistes de reconversion et évolution'}
        ],
        'cv_and_offer': [
            {'id': 5, 'name': 'Gap Analysis', 'description': 'Écarts CV vs poste ciblé'},
            {'id': 6, 'name': 'Optimisation ATS', 'description': 'Mots-clés et compatibilité ATS'},
            {'id': 7, 'name': 'Lettre de motivation', 'description': 'Draft personnalisé'},
            {'id': 8, 'name': 'Pitch "Parlez-moi de vous"', 'description': 'Versions 30s, 2-3min, 5min'},
            {'id': 9, 'name': 'Dans la tête du recruteur', 'description': 'Récit narratif du recruteur'},
            {'id': 10, 'name': 'Questions d\'entretien', 'description': '12 questions types avec réponses'},
            {'id': 11, 'name': 'Veille entreprise', 'description': 'Fiche sur l\'entreprise cible'}
        ]
    }
    return jsonify(modules)

@app.route('/api/analyze', methods=['POST'])
def analyze_cv():
    cv_path = None
    job_path = None
    try:
        api_key = request.form.get('api_key') or os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            return jsonify({'error': 'API key is required'}), 400
        if 'cv' not in request.files:
            return jsonify({'error': 'CV file is required'}), 400
        cv_file = request.files['cv']
        if cv_file.filename == '':
            return jsonify({'error': 'No CV file selected'}), 400
        if not allowed_file(cv_file.filename):
            return jsonify({'error': 'Invalid CV file type'}), 400
        analysis_type = request.form.get('analysis_type', 'complete')
        modules = request.form.get('modules', '').split(',') if request.form.get('modules') else []
        cv_filename = secure_filename(cv_file.filename)
        cv_path = os.path.join(UPLOAD_FOLDER, f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{cv_filename}")
        cv_file.save(cv_path)
        message_content = []
        if cv_filename.endswith(('.pdf', '.png', '.jpg', '.jpeg')):
            cv_base64 = file_to_base64(cv_path)
            media_type = get_media_type(cv_filename)
            if media_type == 'application/pdf':
                message_content.append({"type": "document", "source": {"type": "base64", "media_type": media_type, "data": cv_base64}})
            else:
                message_content.append({"type": "image", "source": {"type": "base64", "media_type": media_type, "data": cv_base64}})
        else:
            with open(cv_path, 'r', encoding='utf-8') as f:
                message_content.append({"type": "text", "text": f"CV:\n{f.read()}"})
        job_offer = None
        if 'job_offer' in request.files:
            job_file = request.files['job_offer']
            if job_file.filename != '' and allowed_file(job_file.filename):
                job_filename = secure_filename(job_file.filename)
                job_path = os.path.join(UPLOAD_FOLDER, f"job_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{job_filename}")
                job_file.save(job_path)
                if job_filename.endswith('.pdf'):
                    message_content.append({"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": file_to_base64(job_path)}})
                else:
                    with open(job_path, 'r', encoding='utf-8') as f:
                        message_content.append({"type": "text", "text": f"Offre d'emploi:\n{f.read()}"})
                job_offer = "provided"
        prompt = f"Génère le dossier IAMonJob avec uniquement les modules suivants: {', '.join(modules)}" if analysis_type == 'custom' and modules else "Génère le dossier IAMonJob complet pour ce CV"
        if job_offer:
            prompt += " et cette offre d'emploi"
        message_content.append({"type": "text", "text": prompt})
        from anthropic import Anthropic
        client = Anthropic(api_key=api_key)
        response = client.messages.create(model="claude-sonnet-4-5-20250929", max_tokens=8000, messages=[{"role": "user", "content": message_content}])
        result_text = "\n".join([block.text for block in response.content if block.type == "text"])
        return jsonify({'success': True, 'analysis': result_text, 'timestamp': datetime.now().isoformat(), 'modules_generated': modules if modules else 'all', 'job_offer_included': bool(job_offer)})
    except Exception as e:
        import traceback
        return jsonify({'error': f'Server error: {str(e)}', 'type': 'server_error', 'details': traceback.format_exc() if os.environ.get('FLASK_ENV') == 'development' else None}), 500
    finally:
        if cv_path and os.path.exists(cv_path):
            try: os.remove(cv_path)
            except: pass
        if job_path and os.path.exists(job_path):
            try: os.remove(job_path)
            except: pass

# FRONTEND ROUTES EN DERNIER
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    if path.startswith('api/'):
        return jsonify({'error': 'API endpoint not found'}), 404
    try:
        return send_from_directory('../frontend', path)
    except:
        return send_from_directory('../frontend', 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV', 'production') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)
