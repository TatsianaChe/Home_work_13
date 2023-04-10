# Scraper.py
import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cars_.csv'
HOST = 'https://av.by'
URL = 'https://cars.av.by/toyota/rav4'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/16.4 Safari/605.1.15'
}


def get_html(url, params=' '):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='listing-item')
    cars = []

    for item in items:
        cars.append(
            {
                'title': item.find('h3',class_="listing-item__title").get_text(strip=True).replace("\xa0", " "),
                'link_cars': HOST + item.find('div', class_="listing-item__about").find('a').get('href'),
                'price': item.find('div', class_="listing-item__prices").text.replace("\xa0", " "),
                'params': item.find('div', class_="listing-item__params").get_text(strip=True)
            }
        )
    return cars


def save_doc(items, path):
    with open('cars_.cvs', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название модели', 'Ссылка на автомобиль:', 'Цена :', 'Параметры:'])
        for item in items:
            writer.writerow([item['title'], item['link_cars'], item['price'], item['params']])


def parser():
    PAGENATION = input('Укажите количество страниц для парсинга:')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        for page in range(1, PAGENATION+1):
            print(f'Парсим страницу:{page}')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
            save_doc(cars, csv)
    else:
        print('Error')


parser()
