f = open("lyrics.txt","w")
f.write("Hello How are you?")
f.close()

f = open("lyrics.txt")
print(f.tell())

data=f.read(10)
print(f.tell())
f.close()