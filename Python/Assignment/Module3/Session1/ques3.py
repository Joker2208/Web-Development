# f = open("my_fav_song.txt","a")
# songs = ["The Weeknd \n","Enigma \n"]
# f.writelines(songs)
# f.close()

f=open("my_fav_song.txt","r")
data = f.readlines()
for i in enumerate(data):
    print(i)

f.close()
