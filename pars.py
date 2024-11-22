import requests
from bs4 import BeautifulSoup

url = "https://www.ozon.ru/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Пример поиска категорий
categories = soup.find_all('a', class_='category-link')
for category in categories:
    print(category.text, category['href'])  # Название и ссылка на категорию
