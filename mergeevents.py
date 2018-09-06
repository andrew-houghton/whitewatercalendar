import scrape
import showevents
from pprint import pprint
from datetime import datetime


def to_bloody_datetime(date):
    if ":" == date[-3:-2]:
        date = date[:-3] + date[-2:]
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=None)


def strip_event_details(calendar_event):
    return {
        'start': to_bloody_datetime(calendar_event['start']['dateTime']),
        'end': to_bloody_datetime(calendar_event['end']['dateTime']),
        'summary': calendar_event['summary'],
        'id': calendar_event['id'],
    }


def flatten_website_sessions(website_events):
    outlist = []
    for day in website_events:
        outlist += day['sessions']
    return outlist


def merge(calendar_events, website_events):
    calendar_events = list(map(strip_event_details, calendar_events))
    website_events = flatten_website_sessions(website_events)

    # For each item in the website look for it on the calendar.
    for c_ind in range(len(calendar_events)):
        for w_ind in range(len(website_events)):
            c_event = calendar_events[c_ind]
            w_event = website_events[w_ind]

            pprint(c_event)
            print('')
            pprint(w_event)
            print('')
            break
        break
    # If it exists delete both copies

if __name__ == '__main__':
    merge(showevents.main(), scrape.main())
