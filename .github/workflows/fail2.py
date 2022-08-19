import re


text_file = open("abc1.txt", "r")


match = re.search(r"^has exceeded threshold limit for messages. Please take action!$", text_file.read())
print(match)
       
text_file.close()
