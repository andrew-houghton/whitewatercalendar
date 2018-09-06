## Calendar Sync for Penrith Whitewater

This script scrapes data from penrith whiteater website about future kayaking days and publishes it on a google calendar.

### Control flow

1. Get current events in calendar.
2. Get events from penrith website.
3. Crop events outside 3 month window.
4. For each day with an event on website update calendar events for that day.
5. Remove calendar events not found on website.
