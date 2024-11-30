#Завдання не зовсім вийшло, можливо сайт блокує, але воно має працювати спочатку знайти інформацію з сайту про погоду,
# програма візьме день неділі і місяця, і погоду(хмарно, ясно, сонячно, вітряно і тд) в один table названий "date & time"
#і візьме темературу та розмістить її в другий table названий "temperature", ці 2 table находяться в ДБ "weather.db". Назви функцій і змінних повязані з книжками через те,
#що код був взятий з мого попереднього проекту.


import sqlite3
import requests
from bs4 import BeautifulSoup

url = "https://weather.com/uk-UA/weather/tenday/l/Zhytomyr+Zhytomyr+Oblast?canonicalCityId=9a3b9955c26967ab4fdf6a1386d68b0af56865b3059665ebbfbf3e11d368c992"
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

def get_book_titles(soup):
    titles = [book.get_text() for book in soup.find_all('h2')]
    return titles

def get_book_prices(soup):
    prices = [price.get_text().replace('Â', '') for price in soup.find_all('span', class_='DetailsSummary--temperature--YGmQ5')]
    return prices

def get_books_info(soup):
    books_info = []
    books = soup.find_all('summary', class_='Disclosure--Summary--kMIqY DaypartDetails--Summary--KWzwv Disclosure--hideBorderOnSummaryOpen--I3oNN"')
    for book in books:
        title = book.find('h2').find['data-testid']
        price = book.find('span', class_='price_color').get_text().replace('Â', '')
        rating = book.find('span', class_='DetailsSummary--extendedData--eJzhb')['class'][1]
        books_info.append({'title': title, 'price': price, 'rating': rating})
    return books_info

titles = get_book_titles(soup)
prices = get_book_prices(soup)
books_info = get_books_info(soup)

connection = sqlite3.connect('weather.db', 5)
cursor = connection.cursor()
connection.commit()

cursor.execute(
     'insert into first_table (date & time) values (titles);'
)
connection.commit()

cursor.execute(
    'insert into first_table (date & time) values (books_info);'
)
connection.commit()

cursor.execute(
    'insert into second_table (temperature) values (prices);'
)
connection.close()
