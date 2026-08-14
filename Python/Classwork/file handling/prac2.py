f=open("Read Method.txt","w")
l=["Hello Python \n","How phyton \n","Web Development \n","Programming \n","Logic"]
f.writelines(l)
f.close()

f = open("Read Method.txt")
data = f.readlines()
for i in data:
    print(len(i))

f.close()