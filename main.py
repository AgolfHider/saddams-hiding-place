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
connection.close()import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://weather.com/uk-UA/weather/tenday/l/Zhytomyr+Zhytomyr+Oblast?canonicalCityId=9a3b9955c26967ab4fdf6a1386d68b0af56865b3059665ebbfbf3e11d368c992"

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

def get_temperature_data(soup):
    days = soup.find_all('h2', class_='DetailsSummary--daypartName--1Mebr') 
    temperatures = soup.find_all('span', class_='DetailsSummary--tempValue--1K4ka') 

    weather_data = []
    for day, temp in zip(days, temperatures):
        weather_data.append({
            'date': day.get_text(),
            'temperature': temp.get_text().replace('°', '')
        })
    return weather_data

weather_data = get_temperature_data(soup)

connection = sqlite3.connect('weather.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time TEXT,
    temperature TEXT
)
''')

for data in weather_data:
    cursor.execute('''
    INSERT INTO weather_data (date_time, temperature)
    VALUES (?, ?)
    ''', (data['date'], data['temperature']))

connection.commit()
connection.close()

