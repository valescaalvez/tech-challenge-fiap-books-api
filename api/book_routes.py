from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required

book_bp = Blueprint('books', __name__, url_prefix='/api/v1/books')

@book_bp.route('', methods=['GET'])
@jwt_required()
def get_all_books():
    books = current_app.data_loader.get_all_books()
    return jsonify(books), 200

@book_bp.route('/<int:book_id>', methods=['GET'])
@jwt_required()
def get_book_by_id(book_id):
    book = current_app.data_loader.get_book_by_id(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

@book_bp.route('/search', methods=['GET'])
@jwt_required()
def search_books():
    title = request.args.get('title')
    category = request.args.get('category')
    books = current_app.data_loader.search_books(title, category)
    return jsonify(books), 200

@book_bp.route('/top-rated', methods=['GET'])
@jwt_required()
def top_rated_books():
    top_books = current_app.data_loader.get_top_rated_books()
    return jsonify(top_books), 200

@book_bp.route('/price-range', methods=['GET'])
@jwt_required()
def price_range_books():
    min_price = request.args.get('min', type=float)
    max_price = request.args.get('max', type=float)
    if min_price is None or max_price is None:
        return jsonify({"error": "Both min and max parameters are required"}), 400
    books = current_app.data_loader.get_books_in_price_range(min_price, max_price)
    return jsonify(books), 200

@book_bp.route('/categories', methods=['GET'])
@jwt_required()
def get_categories():
    categories = current_app.data_loader.get_categories()
    return jsonify(categories), 200
