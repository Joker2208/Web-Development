for i in range(5):
    for j in range(5-i):
        print(" ",end="")

    for k in range(i+1):
        if k==0 or k==i:
            print("* ",end="")
        else:
             print("  ",end="")

    print()

for i in range(3,-1,-1):
        for j in range(5-i):
            print(" ",end="")

        for k in range(i+1):
            if k==0 or k==i:
                print("* ",end="")
            else:
                 print("  ",end="")

        print()