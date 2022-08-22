import time
import datetime
from pytz import timezone


eastern = timezone('US/Eastern')
now = datetime.datetime.now()
minute= now.astimezone(timezone('US/Eastern')).strftime("%M")
print(minute)
