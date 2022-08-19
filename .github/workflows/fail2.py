import re


text_file = open("abc1.txt", "r")
print(text_file.read())
pattern = re.compile(r'has exceeded threshold limit for messages. Please take action!')

match = pattern.search(text_file.read())
if match.group(0):
       print('Match')

       
text_file.close()
