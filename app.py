from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Carrega o CSV ao iniciar
df_books = pd.read_csv('data/books.csv')
df_books['id'] = df_books.index  # cria um id único baseado no index

@app.route('/api/v1/health')
def health():
    return jsonify({'status': 'ok'})

@app.route('/api/v1/books')
def get_books():
    books = df_books.to_dict(orient='records')
    return jsonify(books)

# Exemplo de rota para detalhes por ID
@app.route('/api/v1/books/<int:book_id>')
def get_book(book_id):
    book = df_books[df_books['id'] == book_id]
    if book.empty:
        return jsonify({'error': 'Livro não encontrado'}), 404
    return jsonify(book.iloc[0].to_dict())

# Rota para buscar livros por título e/ou categoria
@app.route('/api/v1/books/search')
def search_books():
    title = request.args.get('title', '').lower()
    category = request.args.get('category', '').lower()
    filtered = df_books
    if title:
        filtered = filtered[filtered['titulo'].str.lower().str.contains(title)]
    if category:
        filtered = filtered[filtered['categoria'].str.lower().str.contains(category)]
    return jsonify(filtered.to_dict(orient='records'))

# Lista todas as categorias únicas
@app.route('/api/v1/categories')
def get_categories():
    categories = df_books['categoria'].unique().tolist()
    return jsonify(categories)

if __name__ == '__main__':
    app.run(debug=True)
