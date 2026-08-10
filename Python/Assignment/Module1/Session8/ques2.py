def extract_artist(song_title):
    index = song_title.index("-")

    artist = index+2
    return song_title[artist:]

print(extract_artist("Blinding Lights - The Weeknd"))
