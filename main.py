import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.geeksforgeeks.org/python/python-web-scraping-tutorial/")
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())