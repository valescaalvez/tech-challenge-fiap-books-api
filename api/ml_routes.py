from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required

ml_bp = Blueprint('ml', __name__, url_prefix='/api/v1/ml')

RATING_MAP = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

@ml_bp.route('/features', methods=['GET'])
@jwt_required()
def ml_features():
    features = current_app.data_loader.get_ml_features()
    return jsonify(features), 200

@ml_bp.route('/training-data', methods=['GET'])
@jwt_required()
def ml_training_data():
    training = current_app.data_loader.get_ml_training_data()
    return jsonify(training), 200

@ml_bp.route('/predictions', methods=['POST'])
@jwt_required()
def ml_predict():
    data = request.get_json() or []
    predictions = []
    for item in data:
        features = item.get('features', {})
        raw_rating = features.get('rating')
        rating_num = RATING_MAP.get(raw_rating, 0) if isinstance(raw_rating, str) else raw_rating or 0
        price = features.get('price', 0)
        pred_label = "recommended" if rating_num >= 4 else "not recommended"
        confidence = 0.95 if rating_num >= 4 else 0.85
        predictions.append({
            "book_id": item.get('book_id'),
            "prediction": pred_label,
            "confidence": confidence
        })
    return jsonify(predictions), 200

