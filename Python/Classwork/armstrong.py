for i in range(100,1000):
    sum = 0
    temp = i

    while temp > 0:
        rem=temp%10
        sum+=(pow(rem,3))
        i = temp//10

        if sum==i:
            print(f"{i} is an armstrong number")

        else:
            pass