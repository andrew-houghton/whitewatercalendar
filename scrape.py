import requests
import bs4

# SCRAPING_URL = "http://www.penrithwhitewater.com.au/water-times-and-events"
# html_doc = requests.get(SCRAPING_URL).text
with open('content.html', 'r') as handle:
    html_doc = handle.read()

print(html_doc)
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup)
