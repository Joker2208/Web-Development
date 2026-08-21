class Song:
    def __init__(self,title,artist,duration):
        self.title = title 
        self.artist= artist
        self.duration = duration

s  = Song("God's plan","Drake",6.45)
s1 = Song("Shooter",'J Cole',4.50)

print(s.title)
print(s1.artist)