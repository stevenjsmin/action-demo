import requests
from bs4 import BeautifulSoup

url = 'https://ridibooks.com/category/bestsellers/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# bookservices = soup.select('.title_text')
bookservices = soup.select('.fig-16r7kln')
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())
