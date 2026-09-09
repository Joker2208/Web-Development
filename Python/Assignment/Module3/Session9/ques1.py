import re

email =  input("Enter your email:")
final = re.match("^[a-z][a-zA-Z0-9._]*@gmail.com$",email)
if final:
    print("Valid Email")
else:
    print("Invalid Email")