str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

lstr1 = set(str1.lower())
lstr2 = set(str2.lower())

common = lstr1 & lstr2

letters = []
for ch in common:
    if ch.isalpha():
        letters.append(ch)

print(sorted(letters))