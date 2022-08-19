import re


text_file = open("abc1.txt", "r+")
str = text_file.read()
#print(str)

match = re.search(r"^has exceeded threshold limit for messages. Please take action!$", str)
if match:
    print("hitting case")
    print('match')
       
text_file.close()
