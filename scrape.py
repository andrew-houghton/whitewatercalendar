import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import date
from datetime import datetime
from time import strptime
from functools import partial


# SCRAPING_URL = "http://www.penrithwhitewater.com.au/water-times-and-events"
# html_doc = requests.get(SCRAPING_URL).text
with open('content.html', 'r') as handle:
    html_doc = handle.read()

soup = BeautifulSoup(html_doc, 'html.parser')
events_section = soup.find_all("div", class_="events-table")[0]
events = events_section.find_all("div", class_="daily-entry")

all_days = []

for day in events:
    if not day.findAll(text='Please call 02 4730 4333 to check water availability.'):
        day_info = {'sessions': []}

        # Get date info
        day_info['month'] = day.find_all("span", class_="month")[
            0].find(text=True)
        day_info['day_num'] = day.find_all("span", class_="day")[
            0].find(text=True)
        all_days.append(day_info)

        # Get event info
        for session in day.find_all("div", class_="item"):
            session_info = {}

            # Get start and finish time
            session_info['start'] = session.find_all("span", class_="start")[
                0].find(text=True)
            session_info['end'] = session.find_all("span", class_="end")[
                0].find(text=True)
            # Get event description
            session_info['description'] = session.find_all("p")[
                1].find(text=True)

            day_info['sessions'].append(session_info)


def handle_times(session, day_date):
    session['start_datetime'] = datetime.combine(
        day_date, datetime.strptime(session['start'], '%H:%M').time())
    session['end_datetime'] = datetime.combine(
        day_date, datetime.strptime(session['end'], '%H:%M').time())
    return session


def handle_dates(day):
    # Get date of day
    day['date'] = date(2018, strptime(
        day['month'], '%b').tm_mon, int(day['day_num']))
    # Add time values for sessions
    map_function = partial(handle_times, day_date=day['date'])
    day['sessions'] = map(map_function, day['sessions'])
    return day

all_days = map(handle_dates, all_days)

pprint(all_days[0])
