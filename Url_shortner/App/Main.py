from flask import Blueprint, request, jsonify, redirect
from .services import generate_short_code, db, increment_click, get_url_info, validate_url

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def health():
    return jsonify({'status': 'Running'}), 200

@main_bp.route('/api/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    long_url = data.get('url')
    if not validate_url(long_url):
        return jsonify({'error': 'Invalid URL'}), 400
    short_code = generate_short_code(long_url)
    return jsonify({'short_code': short_code, 'short_url': f'http://localhost:5000/{short_code}'}), 201

@main_bp.route('/<short_code>')
def redirect_url(short_code):
    url = db.get(short_code)
    if not url:
        return jsonify({'error': 'Not found'}), 404
    increment_click(short_code)
    return redirect(url['original_url'])

@main_bp.route('/api/stats/<short_code>')
def stats(short_code):
    url = get_url_info(short_code)
    if not url:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(url), 200
  
