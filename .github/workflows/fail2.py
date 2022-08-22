
text_file = open("abc1.txt", "r")
readfile = text_file.read()

string1 = "has exceeded threshold limit for messages. Please take action!"
string2 = "There might be problem with WAS servers"
string3 = "Issue Has Occurred for Allowed Retrial Times"
string4 = "Following Queues are not reducing"
string5 = "Following Buses might be down"


if string1 in readfile:
  print(string1)
elif string2 in readfile:
  print(string2)
elif string3 in readfile:
  print(string3)
elif string4 in readfile:
  print(string4)
elif string5 in readfile:
  print(string5)
else:
  print('No Match')
          
text_file.close()
