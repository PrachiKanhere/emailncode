import re


text_file = open("abc1.txt", "r")


if re.search(r"^has exceeded threshold limit for messages. Please take action!$", text_file.read()):
       print('Match')

       
text_file.close()
