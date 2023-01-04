# Päivämäärien käsittely
from datetime import datetime, timezone, timedelta
from time import time
from datetime import date
from zoneinfo import ZoneInfo

today = date.today()
print("Today's date:", today)

print("the current time is: ", datetime.now(tz=timezone.utc))
print("the current timestamp is: ", time())

time_list = [
    datetime(year=2022, month=3, day=21, hour=9, minute=49, second=27),
    datetime.fromisoformat("2022-07-27 09:39:27"),
    datetime(year=2022, month=4, day=21, hour=10, minute=49,
             second=27, tzinfo=timezone.utc),
    datetime(year=2022, month=5, day=21, hour=10, minute=49,
             second=27, tzinfo=timezone.utc),
    datetime.fromtimestamp(10, tz=timezone.utc),
    datetime.fromtimestamp(time(), tz=ZoneInfo("Europe/Helsinki")),
]

for date in time_list:
    print(repr(date))

person_birthday = datetime.fromisoformat("2000-01-01")
birthday_str = datetime.strftime(person_birthday, '%d.%m.%Y')
person_age = datetime.now() - person_birthday
print(f"Ikä nyt {':'.join(str(person_age).split(',')[:1])}"
      f", kun syntynyt {birthday_str}.")


def get_next_christmas(current_date):
    next_xmas = datetime(current_date.year, 12, 24)
    i = 0
    while next_xmas < current_date:
        next_xmas = datetime(current_date.year + i, 12, 24)
        i += 1
    return next_xmas


weekday_map = {0: 'Maanantai', 1: 'Tiistai', 2: 'Keskiviikko',
               3: 'Torstai', 4: 'Perjantai', 5: 'Lauantai',
               6: 'Sunnuntai'}

next_christmas = get_next_christmas(datetime.now())
print(f"Seuraava joulu {next_christmas} on viikonpäivänä " +
      f"{weekday_map[next_christmas.weekday()]}.")
person_age = next_christmas - datetime.now()
print(f"Jouluun aikaa {':'.join(str(person_age).split(',')[:1])}.")

today = date.now()
print(today.strftime("%d.%m.%y"))
print(today.strftime("%d.%m.%Y"))

print(today.strftime("%B %d, %Y"))

print(today.strftime("%b-%d-%Y"))

now = datetime.now()
print(now.strftime("%c"))
print(now.strftime("%x %X"))
print(now.strftime("%d.%m.%Y %H:%M:%S"))


def locale_finnish():
    import locale
    locale.setlocale(locale.LC_TIME, 'fi_FI')

    now = datetime.now()
    print(now.strftime("%d. %Bta vuonna %Y."))
    print(now.strftime("%c"))
    print(now.strftime("%x %X"))
    print(now.strftime("%d.%m.%Y %H:%M:%S"))


locale_finnish()


def locale_sweden():
    import locale
    locale.setlocale(locale.LC_TIME, 'sv_SE')

    now = datetime.now()
    print(now.strftime("%d. %B %Y."))
    print(now.strftime("%c"))
    print(now.strftime("%x %X"))
    print(now.strftime("%d.%m.%Y %H:%M:%S"))


locale_sweden()
