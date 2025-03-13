import requests
from bs4 import BeautifulSoup


url = "https://example.com"
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
print(soup.title.string)
print(soup.text)
