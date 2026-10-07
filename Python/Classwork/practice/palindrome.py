og = input("Enter: ")
og = og.replace(" ","")
og.lower()
rev = og[::-1]

if rev == og:
    print("yes")
else:
    print("no")