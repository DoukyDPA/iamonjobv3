FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY backend/ .
COPY frontend/ ../frontend/

# Create necessary directories
RUN mkdir -p uploads outputs

# Expose port
EXPOSE 5000

# Environment variables
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1
ENV PORT=5000

# Run the application with gunicorn - TIMEOUT 180s pour les analyses longues
CMD gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 180 --graceful-timeout 180 --keep-alive 5 --access-logfile - --error-logfile - app:app
