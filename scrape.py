import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import date
from datetime import datetime
from time import strptime
from functools import partial


def get_soup():
    # SCRAPING_URL = "http://www.penrithwhitewater.com.au/water-times-and-events"
    # html_doc = requests.get(SCRAPING_URL).text
    with open('content.html', 'r') as handle:
        html_doc = handle.read()
    return BeautifulSoup(html_doc, 'html.parser')


def get_day_html_array(soup):
    events_section = soup.find_all("div", class_="events-table")[0]
    return events_section.find_all("div", class_="daily-entry")


def process_session_html(soup):
    return {
        'start': soup.find_all("span", class_="start")[0].find(text=True),
        'end': soup.find_all("span", class_="end")[0].find(text=True),
        'description': soup.find_all("p")[1].find(text=True)
    }


def extract_date_from_html(soup):
    month = soup.find_all("span", class_="month")[0].find(text=True)
    day = soup.find_all("span", class_="day")[0].find(text=True)
    return (month, day)


def process_day_html(soup):
    if soup.findAll(text='Please call 02 4730 4333 to check water availability.'):
        return None
    day_info = {}
    day_info['month'], day_info['day_num'] = extract_date_from_html(soup)
    day_info['sessions'] = map(process_session_html, soup.find_all("div", class_="item"))
    return day_info


days_html = get_day_html_array(get_soup())
days_data = [x for x in map(process_day_html,days_html) if x is not None]


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

days_data = map(handle_dates, days_data)

pprint(days_data)
