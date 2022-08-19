import re


text_file = open("abc1.txt", "r")


if re.search(r".*", text_file.read()):
       print('Match')

       
text_file.close()
