import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

BASE_URL = "https://books.toscrape.com/"
BOOKS = []

def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def extract_book_data(book, category):
    title = book.h3.a['title']
    url = BASE_URL + book.h3.a['href'].replace('../', '')
    raw_price = book.select_one('.price_color').text
    price = re.sub(r'[^\d.]', '', raw_price)
    rating = book.select_one('p.star-rating')['class'][1]
    stock = book.select_one('.availability').text.strip()
    image_url = BASE_URL + book.img['src'].replace('../', '')
    return {
        'titulo': title,
        'preco': float(price),
        'avaliacao': rating,
        'estoque': stock,
        'categoria': category,
        'url_imagem': image_url,
        'url_livro': url
    }

def scrape_category(category_url, category):
    page_url = category_url
    while True:
        print(f"Raspando: {page_url}")
        soup = get_soup(page_url)
        books = soup.select('article.product_pod')
        for book in books:
            BOOKS.append(extract_book_data(book, category))
        next_btn = soup.select_one('li.next > a')
        if next_btn:
            next_page = next_btn['href']
            page_url = '/'.join(page_url.split('/')[:-1]) + '/' + next_page
            time.sleep(0.5)
        else:
            break

def main():
    homepage = get_soup(BASE_URL)
    category_links = homepage.select('.nav-list ul li a')
    for cat in category_links:
        category = cat.text.strip()
        cat_url = BASE_URL + cat['href']
        scrape_category(cat_url, category)
    # Salva em CSV
    df = pd.DataFrame(BOOKS)
    df.to_csv('data/books.csv', index=False, encoding='utf-8')
    print(f"{len(BOOKS)} livros salvos em data/books.csv")

if __name__ == "__main__":
    main()
