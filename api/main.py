from fastapi import FastAPI
from typing import List, Dict
import csv
import os

app = FastAPI()

BOOKS_CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'books.csv')

def load_books() -> List[Dict]:
    books = []
    with open(BOOKS_CSV_PATH, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            row["id"] = idx  # Adiciona um id único para cada livro (baseado na ordem)
            books.append(row)
    return books

@app.get("/api/v1/books")
def get_books():
    books = load_books()
    return books