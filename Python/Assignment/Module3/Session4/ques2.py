class SongAlreadyExistsError(Exception):
    pass

playlist = ["Winner takes it all","Gods Plan","Interstellar"]
song = input("Enter song:")

def add_song_to_playlist(song):
    try:
        if song in playlist:
            raise SongAlreadyExistsError(song)
        else:
            print("Song Added")
    except SongAlreadyExistsError as s:
        print(s,",Song exists")

add_song_to_playlist(song)
