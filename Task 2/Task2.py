import requests
from bs4 import BeautifulSoup
import csv
import os

url = 'https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article', class_='product_pod')

data = []

for book in books:
    title = book.find('h3').find('a')['title']
    price_element = book.find('p', class_='price_color')  # Correct class name
    if price_element:
        price = price_element.get_text(strip=True)
    else:
        price = "Price not found"
    availability = book.find('p', class_='instock availability').get_text(strip=True)

    data.append([title, price, availability])

csv_filename = 'books.csv'

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, csv_filename)

with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Title', 'Price', 'Availability'])
    csv_writer.writerows(data)

print(f'Data has been scraped and saved to {output_path}')