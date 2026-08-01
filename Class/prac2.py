num = int(input("Enter a number: "))

if num%3 ==0  and num%5 == 0:
    print("Number is divisble by both 3 and 5")

elif num%5 == 0:
    print("Number is divisible by 5")

elif num%3 == 0:
    print("Number is divisible by 3")

else:
    print(num)