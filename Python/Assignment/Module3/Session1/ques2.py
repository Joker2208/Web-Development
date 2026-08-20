f=open("my_fav_song.txt","r")
data = f.readlines()
for i in enumerate(data):
    print(i)

f.close()
