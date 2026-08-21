f = open("playlist.txt","w")
songs = ["God's Plan \n","Arz kiya hai, Anuv jain\n","Bling \n"]
f.writelines(songs)
f.close()

f = open("playlist.txt")
f.readline()
f.readline()
pos = f.tell()
f.close()

f= open("playlist.txt")
(f.seek(pos))
data = f.readline()
print(data)
