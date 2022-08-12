import time
import datetime
from pytz import timezone
import re


text_file = open("abc1.txt", "r")
str = text_file.read()
print(str)
eastern = timezone('US/Eastern')
Day_of_week = datetime.date.today().strftime("%A")
Month_of_year=datetime.date.today().strftime("%B")
Day_of_the_month=datetime.date.today().strftime("%d")
now = datetime.datetime.now()
est_time= now.astimezone(timezone('US/Eastern')).strftime("%H:%M:%S")
zone = datetime.datetime.now(eastern).strftime("%Z")
Current_year=datetime.date.today().strftime("%Y")
TIMESTAMP= Day_of_week[0:3]+' '+Month_of_year[0:3]+' '+Day_of_the_month+' '+est_time+' '+zone+' '+Current_year
print(TIMESTAMP)

formattedDate = datetime.date.today().strftime("%d-%b-%Y")
print(formattedDate)

match = re.search(r"Following Buses might be down: \[.*\]", str)
if match:
       downBus= match.group()
       print(downBus)
       DOWN_BUS = downBus.split(": ")[1]
       print(DOWN_BUS)
       if len(DOWN_BUS)== 0:
           print('Down Bus not defined')
else:
    print('Message Engines up and running')
text_file.close()

