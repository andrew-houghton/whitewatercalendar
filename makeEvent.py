from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
CALENDAR_ID = 'nhae532jfn0e0qc9ghb0d2s3i8@group.calendar.google.com'


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    event = {
        'summary': 'Whitewater Rafting & Recreational Paddling',
        'location': 'Penrith Whitewater Stadium, McCarthys Ln, Cranebrook NSW 2749, Australia',
        'start': {
            'dateTime': '2018-09-09T10:30:00+10:00',
            'timeZone': 'Australia/Sydney',
        },
        'end': {
            'dateTime': '2018-09-09T15:00:00+10:00',
            'timeZone': 'Australia/Sydney',
        }
    }

    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

if __name__ == '__main__':
    main()
