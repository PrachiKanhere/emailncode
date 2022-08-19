import re


text_file = open("abc1.txt", "r")
str = text_file.read()

if re.search(r"has exceeded threshold limit for messages. Please take action!",str):
       print('Match')

       
text_file.close()
