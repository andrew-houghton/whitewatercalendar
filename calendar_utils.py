from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CALENDAR_ID = 'nhae532jfn0e0qc9ghb0d2s3i8@group.calendar.google.com'


def get_creds():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return build('calendar', 'v3', http=creds.authorize(Http()))


def event_list():
    service = get_creds()
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=now, singleEvents=True,
                                          orderBy='startTime').execute()
    return events_result.get('items', [])


def delete(event_id):
    service = get_creds()
    service.events().delete(calendarId=CALENDAR_ID, eventId=event_id).execute()


def add(event_details):
    service = get_creds()
    event = {
        'summary': event_details['description'],
        'location': 'Penrith Whitewater Stadium, McCarthys Ln, Cranebrook NSW 2749, Australia',
        'start': {
            'dateTime': event_details['start'].isoformat(),
            'timeZone': 'Australia/Sydney',
        },
        'end': {
            'dateTime': event_details['end'].isoformat(),
            'timeZone': 'Australia/Sydney',
        }
    }
    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

if __name__ == '__main__':
    pprint(event_list())
