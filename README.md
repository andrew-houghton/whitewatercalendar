## Calendar Sync for Penrith Whitewater

This script scrapes data from penrith whiteater website about future kayaking days and publishes it on a google calendar.

### Control flow

1. Get current events in calendar.
2. Get events from penrith website.
3. If events from the website are already in the calendar ignore them.
4. Otherwise delete the old events on the calendar and add all the new events.
