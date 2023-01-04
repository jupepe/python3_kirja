# Esimerkki: päivämäärät ja aikavyöhykkeet
from datetime import datetime

current_time = datetime.now()
print(current_time)
print(repr(current_time))
print("Aikavyöhyke:", current_time.tzinfo)
print("UTC:", current_time.utcnow())

from zoneinfo import ZoneInfo

timezone_fi = ZoneInfo("Europe/Helsinki")
print("Suomen ajassa:", current_time.astimezone(timezone_fi))

timezone_se = ZoneInfo("Europe/Stockholm")
print("Ruotsin ajassa:", current_time.astimezone(timezone_se))

tz_lh = ZoneInfo("Australia/Lord_Howe")
print("Eräs Australian aikavyöhyke:", current_time.astimezone(tz_lh))
