from flask import Blueprint, jsonify, request
import csv
import os

routes = Blueprint('routes', __name__)

def load_books_from_csv(file_path):
    books = []
    abs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), file_path)
    with open(abs_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader):
            row['id'] = str(idx)  # Gera um ID único baseado no índice da linha
            books.append(row)
    return books

books = load_books_from_csv('data/books.csv')

# Health Check
@routes.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'API is running'}), 200

# Busca livro por ID
@routes.route('/books/<book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

# Busca por título / categoria
@routes.route('/books/search', methods=['GET'])
def search_books():
    title = request.args.get('title')
    category = request.args.get('category')

    results = books

    if title:
        results = [book for book in results if title.lower() in book['title'].lower()]

    if category:
        results = [book for book in results if category.lower() == book['category'].lower()]

    return jsonify(results)

# Lista todas as categorias únicas
@routes.route('/categories', methods=['GET'])
def get_categories():
    categories = list(set([book['category'] for book in books]))
    return jsonify(categories)
