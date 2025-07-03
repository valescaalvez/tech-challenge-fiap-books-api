from flask import Blueprint, jsonify, request
import pandas as pd
import os

bp = Blueprint('api', __name__, url_prefix='/api/v1')

DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'books.csv'))
df_books = pd.read_csv(DATA_PATH)
df_books['id'] = df_books.index

@bp.route('/health')
def health():
    """
    Healthcheck da API
    ---
    responses:
      200:
        description: API está online
        examples:
          application/json: { "status": "ok" }
    """
    return jsonify({'status': 'ok'})

@bp.route('/books')
def get_books():
    """
    Lista todos os livros disponíveis
    ---
    responses:
      200:
        description: Lista de livros
        schema:
          type: array
          items:
            type: object
    """
    books = df_books.to_dict(orient='records')
    return jsonify(books)

@bp.route('/books/<int:book_id>')
def get_book(book_id):
    """
    Retorna detalhes de um livro específico pelo ID
    ---
    parameters:
      - name: book_id
        in: path
        type: integer
        required: true
        description: ID do livro
    responses:
      200:
        description: Detalhes do livro
        schema:
          type: object
      404:
        description: Livro não encontrado
        examples:
          application/json: { "error": "Livro não encontrado" }
    """
    book = df_books[df_books['id'] == book_id]
    if book.empty:
        return jsonify({'error': 'Livro não encontrado'}), 404
    return jsonify(book.iloc[0].to_dict())

@bp.route('/books/search')
def search_books():
    """
    Busca livros por título e/ou categoria
    ---
    parameters:
      - name: title
        in: query
        type: string
        required: false
        description: Parte do título do livro
      - name: category
        in: query
        type: string
        required: false
        description: Parte da categoria
    responses:
      200:
        description: Livros encontrados
        schema:
          type: array
          items:
            type: object
    """
    title = request.args.get('title', '').lower()
    category = request.args.get('category', '').lower()
    filtered = df_books
    if title:
        filtered = filtered[filtered['titulo'].str.lower().str.contains(title)]
    if category:
        filtered = filtered[filtered['categoria'].str.lower().str.contains(category)]
    return jsonify(filtered.to_dict(orient='records'))

@bp.route('/categories')
def get_categories():
    """
    Lista todas as categorias de livros disponíveis
    ---
    responses:
      200:
        description: Lista de categorias
        schema:
          type: array
          items:
            type: string
    """
    categories = df_books['categoria'].unique().tolist()
    return jsonify(categories)
