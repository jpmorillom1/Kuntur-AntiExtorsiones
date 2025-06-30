from flask import Blueprint, render_template, jsonify
from app.core.threat_detector import extract_keywords

api_blueprint = Blueprint('api_blueprint', __name__)

@api_blueprint.route('/')
def index():
    return render_template('index.html')

@api_blueprint.route('/api/test-transcripcion')
def test_transcripcion():
    texto = "Esto es un intento de extorsión, por favor transfiera dinero"
    keywords = extract_keywords(texto)
    return jsonify({
        "texto": texto,
        "keywords": keywords
    })
