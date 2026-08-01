len1 = float(input("Enter a length: "))
len2 = float(input("Enter a length: "))
len3 = float(input("Enter a length: "))

if len1 + len2 > len3 and len1 + len3 > len2 and len2 + len3 > len1:
    print("Valid Triangle")

else:
    print("InValid Triangle")
