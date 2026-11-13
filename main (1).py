import datetime

TITLE = input("Enter event title: ")
YEAR = int(input("Enter year: "))
MONTH = int(input("Enter month: "))
DAY = int(input("Enter day: "))


event_date = datetime.date(YEAR, MONTH , DAY)
month_day = event_date.strftime("%B")


print("\nFormatted Output:")
print(f"Event: {TITLE.strip().upper()}")
print(f"Date: {month_day} {DAY}, {YEAR}")
print(f"Year: {YEAR}")
print(f"Month: {month_day}")
print(f"Day: {DAY}")
print(f"Weekday: {event_date.strftime("%A")}")