import csv
import os
import statistics

class DataLoader:
    def __init__(self, data_path=None):
        if data_path is None:
            data_path = os.getenv('DATA_PATH', 'data/processed/books.csv')
        if not os.path.isabs(data_path):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            data_path = os.path.join(base_dir, '../..', data_path)
        self.data_path = os.path.normpath(data_path)
        self.books = []
        self.load_data()
    
    def load_data(self):
        try:
            print(f"📂 Carregando dados de: {self.data_path}")
            with open(self.data_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for i, row in enumerate(reader):
                    row['id'] = i
                    try:
                        price_str = row.get('price', '').replace('£', '')
                        row['price_float'] = float(price_str)
                    except (ValueError, KeyError):
                        row['price_float'] = 0.0
                    
                    row['availability'] = 1 if "In stock" in row.get('availability', '') else 0
                    self.books.append(row)
            print(f"✅ Dados carregados com sucesso! Total: {len(self.books)} livros")
        except FileNotFoundError:
            print(f"⚠️ Arquivo não encontrado: {self.data_path}")
            self.books = []
        except Exception as e:
            print(f"❌ Erro ao carregar dados: {str(e)}")
            self.books = []
    
    def get_all_books(self):
        return self.books
    
    def get_book_by_id(self, book_id):
        try:
            book_id = int(book_id)
            return self.books[book_id] if 0 <= book_id < len(self.books) else None
        except (ValueError, IndexError):
            return None
    
    def search_books(self, title=None, category=None):
        results = []
        for book in self.books:
            title_match = not title or title.lower() in book.get('title', '').lower()
            category_match = not category or category.lower() == book.get('category', '').lower()
            if title_match and category_match:
                results.append(book)
        return results
    
    def get_categories(self):
        return sorted({book.get('category', '') for book in self.books})
    
    def get_overview_stats(self):
        if not self.books:
            return {}
        prices = [b['price_float'] for b in self.books]
        ratings = [b.get('rating') for b in self.books]
        rating_distribution = {r: 0 for r in ['One', 'Two', 'Three', 'Four', 'Five']}
        for r in ratings:
            if r in rating_distribution:
                rating_distribution[r] += 1
        return {
            "total_books": len(self.books),
            "average_price": round(statistics.mean(prices), 2) if prices else 0,
            "min_price": round(min(prices), 2) if prices else 0,
            "max_price": round(max(prices), 2) if prices else 0,
            "rating_distribution": rating_distribution
        }
    
    def get_category_stats(self):
        categories = {}
        for book in self.books:
            cat = book.get('category', '')
            stats = categories.setdefault(cat, {"count": 0, "prices": []})
            stats["count"] += 1
            stats["prices"].append(book['price_float'])
        for cat, stats in categories.items():
            prices = stats.pop("prices", [])
            if prices:
                stats["min_price"] = round(min(prices), 2)
                stats["max_price"] = round(max(prices), 2)
                stats["avg_price"] = round(statistics.mean(prices), 2)
        return categories
    
    def get_top_rated_books(self, top_n=10):
        sorted_books = sorted(
        self.books,
        key=lambda x: x.get('rating', ''),
        reverse=True
    )
        return sorted_books[:top_n]
    
    def get_books_in_price_range(self, min_price, max_price):
        return [b for b in self.books if min_price <= b['price_float'] <= max_price]
    
    def get_ml_features(self):
        return [{
            "id": b['id'],
            "title": b.get('title'),
            "price": b['price_float'],
            "rating": b.get('rating'),
            "category": b.get('category'),
            "availability": b.get('availability')
        } for b in self.books]
    
    def get_ml_training_data(self):
        mapping = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        return [{
            "id": b['id'],
            "features": {
                "price": b['price_float'],
                "rating": mapping.get(b.get('rating'), 3),
                "category": b.get('category'),
                "availability": b.get('availability')
            },
            "target": None
        } for b in self.books]

data_loader = DataLoader()