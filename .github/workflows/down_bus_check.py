import re


text_file = open("abc1.txt", "r")
str = text_file.read()
print(str)

match = re.search(r"Following Buses might be down: \[.*\]", str)
if match:
       downBus= match.group()
       DOWN_BUS = downBus.split(": ")[1]
       print(DOWN_BUS)
       if len(DOWN_BUS)== 0:
           print('Down Bus not defined')
else:
       print('Message Engines up and running')
text_file.close()
