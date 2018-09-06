import scrape
import showevents


def merge(calendar_events, website_events):
    print(calendar_events)
    print(website_events)

if __name__ == '__main__':
    merge(showevents.main(), scrape.main())
