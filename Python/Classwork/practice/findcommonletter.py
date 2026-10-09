str1 = input("Enter: ")
str2 = input("Enter:")

s1 = set(str1.lower())
s2 = set(str2.lower())

common = s1 & s2
final = []

for ch in common:
    if ch.isalpha():
      final.append(ch)

print(sorted(final))