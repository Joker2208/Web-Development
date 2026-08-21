f = open("orders.txt","w")
lst = ["Order1 \n","Order2 \n","Order3 \n","Order4 \n","Order5 \n"]
f.writelines(lst)
f.close()

f = open("orders.txt")
while True:
    data = f.readline()
    if data == "":
        break
    print(data,end="")
    print(f.tell(),"\n")


f.close()


