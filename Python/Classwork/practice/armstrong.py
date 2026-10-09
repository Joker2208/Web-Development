num = int(input("Enter num:"))
length = len(str(num))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp = temp // 10

if num == sum:
    print("yes")
else:
    print("no")