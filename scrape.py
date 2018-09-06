import requests
from bs4 import BeautifulSoup
from pprint import pprint

# SCRAPING_URL = "http://www.penrithwhitewater.com.au/water-times-and-events"
# html_doc = requests.get(SCRAPING_URL).text
with open('content.html', 'r') as handle:
    html_doc = handle.read()

soup = BeautifulSoup(html_doc, 'html.parser')
events_section = soup.find_all("div", class_="events-table")[0]
events = events_section.find_all("div", class_="daily-entry")

all_days = []

for event in events:
    if not event.findAll(text='Please call 02 4730 4333 to check water availability.'):
        day_events = {'events': []}

        # Get date info
        day_events['month'] = event.find_all("span", class_="month")[
            0].find(text=True)
        day_events['day'] = event.find_all("span", class_="day")[
            0].find(text=True)
        all_days.append(day_events)

        # Get event info
        for session in event.find_all("div", class_="item"):
            session_data = {}

            # Get start and finish time
            session_data['start'] = session.find_all("span", class_="start")[
                0].find(text=True)
            session_data['end'] = session.find_all("span", class_="end")[
                0].find(text=True)
            # Get event description
            session_data['description'] = session.find_all("p")[
                1].find(text=True)

            day_events['events'].append(session_data)

pprint(all_days)
