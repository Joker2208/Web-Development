f = open("my_fav_song.txt","r")
data=f.readlines()
print("Total Songs: ",len(data))
f.close()