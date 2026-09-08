# import re

# # st = "Sun rises in in the east"

# # k = re.match("in",st)
# # k = re.search("in",st)
# # k = re.findall("in",st)
# # k = re.finditer("in",st)
# # print(next(k))

# # k = re.sub("in","k",st)
# # k = re.split(" ",st)
# # print(k)

# st = "A quick brown fox jumped over a lazy dog,8qe88w87 iheqdh8723, foox, fx"

# # k = re.findall("f.x",st) #only finds if there is a one charac in the middle
# # k = re.search("^fox",st) #to find in start
# # k = re.search("dog$",st) #to find at the end
# # k = re.findall("fo*x",st) #to find all charcs
# # k = re.findall("fo+x",st) #to find one or more repetitions
# # k = re.findall("fo?x",st) #to match 0 or 1 occurence

# # k = re.findall(r"\bcat","cat in catalog")
# # # print(k)

# # phone = "4673563784"
# # k = re.match(r"^\d{10}$",phone)
# # if k is None:
# #     print("invalid phn no")
# # else:
# #     print("Valid Phn no")

# # email = "tops@gmail.com"
# # k = re.match(r"^[a-z0-9]+@[a-z]+\.[a-z]{2,4}$",email)
# # print(k)

# user = "Dipesh"
# k = re.match(r"\D[a-z]{3,11}$",user)
# print(k)
