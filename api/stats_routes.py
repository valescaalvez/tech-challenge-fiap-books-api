from flask import Blueprint, jsonify, current_app
from flask_jwt_extended import jwt_required

stats_bp = Blueprint('stats', __name__, url_prefix='/api/v1/stats')

@stats_bp.route('/overview', methods=['GET'])
@jwt_required()
def overview_stats():
    stats = current_app.data_loader.get_overview_stats()
    return jsonify(stats), 200

@stats_bp.route('/categories', methods=['GET'])
@jwt_required()
def category_stats():
    stats = current_app.data_loader.get_category_stats()
    return jsonify(stats), 200
