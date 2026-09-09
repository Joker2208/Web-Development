import re

str = "ndkjqnq3323243214nmeklnm4"
contact = re.search("\d{10}",str)
numb = contact.group()
print(numb)