str1 = "Music Lover | Foodie | Traveller"
count = 0

for char in str1:
    if char == " ":
        pass
    else:
        count+=1
print(count,end="")