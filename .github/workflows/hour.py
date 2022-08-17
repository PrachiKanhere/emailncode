import datetime
from pytz import timezone

eastern = timezone('US/Eastern')
now = datetime.datetime.now()
hour= now.astimezone(timezone('US/Eastern')).strftime("%H")
print(hour)
