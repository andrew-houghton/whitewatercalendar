import scrape
import calendar
from pprint import pprint
from datetime import datetime


def events_match(c_event, w_event):
    return w_event['start'] == c_event['start'] and w_event['end'] == c_event['end']


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


def set_matched_status(array, status):
    for i in range(len(array)):
        array[i]['match'] = status
    return array


def mark_pairs_matched(calendar_events, website_events):
    # Find matching events
    for c_ind in range(len(calendar_events)):
        c_event = calendar_events[c_ind]
        if not c_event['match']:
            for w_ind in range(len(website_events)):
                w_event = website_events[w_ind]
                if not website_events[w_ind]['match']:
                    if events_match(c_event, website_events[w_ind]):
                        # These events match
                        calendar_events[c_ind]['match'] = True
                        website_events[w_ind]['match'] = True

                if website_events[w_ind]['match']:
                    break
        if calendar_events[c_ind]['match']:
            break
    return (calendar_events, website_events)


def merge(calendar_events, website_events):
    calendar_events = list(map(strip_event_details, calendar_events))
    website_events = flatten_website_sessions(website_events)

    calendar_events = set_matched_status(calendar_events, False)
    website_events = set_matched_status(website_events, False)

    calendar_events, website_events = mark_pairs_matched(calendar_events, website_events)

    # Delete unmatched calendar events
    calendar_delete_ids = [x['id'] for x in calendar_events if not x['match']]

    # Insert new calendar events
    calendar_new_entries = [x for x in website_events if not x['match']]
    pprint(calendar_new_entries)

if __name__ == '__main__':
    merge(calendar.event_list(), scrape.main())
