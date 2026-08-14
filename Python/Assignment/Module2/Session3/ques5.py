title = ["God's Plan","Enigma","Arz Kiya Hai"]
views = [1203.56,567436.8,65343.09875]

def youtube(title,views):
    r=[(title,round(views)) for title,views in zip(title,views)]
    return r

print(youtube(title,views))

