song = {
    "God's plan": 6.45
}

def get_song_duration(name):
    try:
        duration = song[name]
        print(f"{name} : {duration}")
    except KeyError:
        print("Song not found..")

get_song_duration("Shape of you")
get_song_duration("God's plan")
