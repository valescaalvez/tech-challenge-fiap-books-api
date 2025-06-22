from flask import Blueprint, jsonify, request
import csv
import os

routes = Blueprint('routes', __name__)  

def load_books_from_csv(file_path):
    books = []
    abs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), file_path)
    with open(abs_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append(row)
    return books

books = load_books_from_csv('data/books.csv')

@routes.route('/books/search', methods=['GET'])  #
def search_books():
    title = request.args.get('title')
    category = request.args.get('category')

    results = books

    if title:
        results = [book for book in results if title.lower() in book['title'].lower()]

    if category:
        results = [book for book in results if category.lower() == book['category'].lower()]

    return jsonify(results)
