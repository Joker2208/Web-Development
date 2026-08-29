#Write a function to compute the sum of all odd numbers in an array, but skip adding any number that is divisible by  5.


lst = list(map(int,input("Enter numbers: ").split()))

def odd(lst):
    sum = 0
    for i in lst:
        if i % 2 ==0:
            pass
        elif i % 5 ==0:
            pass
        else:
            sum += i
    return sum
print(odd(lst))