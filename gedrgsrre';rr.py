import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

def get_book_titles(soup):
    titles = [book.get_text() for book in soup.find_all('h3')]
    return titles

def get_book_prices(soup):
    prices = [price.get_text().replace('Â', '') for price in soup.find_all('p', class_='price_color')]
    return prices

def get_books_info(soup):
    books_info = []
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').get_text().replace('Â', '')
        rating = book.find('p', class_='star-rating')['class'][1]
        books_info.append({'title': title, 'price': price, 'rating': rating})
    return books_info

titles = get_book_titles(soup)
prices = get_book_prices(soup)
books_info = get_books_info(soup)

print("Назви книг:")
print(titles)

print("\nЦіни книг:")
print(prices)

print("\nІнформація про всі книги:")
for book in books_info:
    print(book)
