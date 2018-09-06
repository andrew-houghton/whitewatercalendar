import requests
from bs4 import BeautifulSoup

# SCRAPING_URL = "http://www.penrithwhitewater.com.au/water-times-and-events"
# html_doc = requests.get(SCRAPING_URL).text
with open('content.html', 'r') as handle:
    html_doc = handle.read()

soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.find_all("div", class_="events-table")[0]
print(table)
