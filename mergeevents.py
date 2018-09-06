import scrape
import showevents
from pprint import pprint


def strip_event_details(calendar_event):
    return {
        'end': calendar_event['end'],
        'start': calendar_event['start'],
        'summary': calendar_event['summary'],
        'id': calendar_event['id'],
    }


def merge(calendar_events, website_events):
    pprint(calendar_events)
    calendar_events = list(map(strip_event_details, calendar_events))
    pprint(calendar_events)

if __name__ == '__main__':
    merge(showevents.main(), scrape.main())
