from flask import Blueprint, render_template, request, jsonify
from db import db  # db 인스턴스 가져오기
from db.connector import Location  # Location 모델 가져오기

maps_bp = Blueprint('maps', __name__)


@maps_bp.route('/save_location', methods=['POST'])
def save_location():
    data = request.json
    new_location = Location(name=data['name'], latitude=data['latitude'], longitude=data['longitude'])
    db.session.add(new_location)
    db.session.commit()
    return jsonify({'message': 'Location saved successfully!'})
