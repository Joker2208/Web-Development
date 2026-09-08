num = 100
flag = 0

for num in range(2,num+1):
    flag=0
    
    for k in range(2,num):
        if num%k==0:
            flag =1
            break

    if flag==0:
        print("Number is prime",num)
    else:
        pass