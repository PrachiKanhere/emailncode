import re


text_file = open("abc1.txt", "r")
print(text_file.read())
pattern = re.compile('has exceeded threshold limit for messages. Please take action!')

match = pattern.search(text_file.read())
if match:
       print('Match')

       
text_file.close()
