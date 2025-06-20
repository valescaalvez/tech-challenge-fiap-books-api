import requests
from bs4 import BeautifulSoup
import csv
import os

BASE_URL = "https://books.toscrape.com/"

def get_category_links():
    res = requests.get(BASE_URL)
    soup = BeautifulSoup(res.text, "html.parser")
    category_links = []
    for cat in soup.select('.side_categories ul li ul li a'):
        link = BASE_URL + cat['href']
        category_links.append(link)
    return category_links

def parse_book(book, category):
    title = book.select_one('h3 a')['title']
    price = book.select_one('.price_color').text.replace('£','').strip()
    availability = book.select_one('.instock.availability').text.strip()
    rating = book.select_one('.star-rating')['class'][1]
    image = BASE_URL + book.select_one('.image_container img')['src'].replace('../', '')
    return [title, price, rating, availability, category, image]

def scrape_books():
    books_data = []
    for cat_url in get_category_links():
        res = requests.get(cat_url)
        soup = BeautifulSoup(res.text, "html.parser")
        category = soup.select_one('div.page-header.action h1').text.strip()
        while True:
            for book in soup.select('.product_pod'):
                books_data.append(parse_book(book, category))
            # Próxima página
            next_btn = soup.select_one('li.next a')
            if next_btn:
                next_url = cat_url.rsplit('/', 1)[0] + '/' + next_btn['href']
                res = requests.get(next_url)
                soup = BeautifulSoup(res.text, "html.parser")
                cat_url = next_url
            else:
                break
    return books_data

def save_to_csv(books_data, filename='data/books.csv'):
    os.makedirs('data', exist_ok=True)  # Garante que a pasta existe
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'price', 'rating', 'availability', 'category', 'image_url'])
        writer.writerows(books_data)

if __name__ == "__main__":
    print("Scraping books.toscrape.com ...")
    books = scrape_books()
    save_to_csv(books)
    print(f"Scraped {len(books)} books! Salvo em data/books.csv")
