num = int(input("Enter:"))
length = len(str(num))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp = temp // 10

if sum == num:
    print("yes")
else:
    print("no")