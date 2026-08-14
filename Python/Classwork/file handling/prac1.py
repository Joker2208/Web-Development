f = open("text.txt","w")
f.write("Hello Python")
f.close()

f=open("text.txt")
data = f.read()
print(data)