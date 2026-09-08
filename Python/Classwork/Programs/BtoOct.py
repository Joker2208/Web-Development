num = int(input("Enter a binary number: "))
sum = 0
p = 0
oct = ""

while num!=0:
    rem = num%10
    sum += (pow(2,p)*rem)
    num = num//10
    p+=1
print(sum)

while sum!=0:
    rem = sum%8
    sum = sum//8
    oct = str(rem) + oct

print(oct)
