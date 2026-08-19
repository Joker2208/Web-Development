def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist

def remove_song(song_name,playlist):
    playlist.remove(song_name)
    return playlist

def display_playlist(playlist):
    for i, song in enumerate(playlist):
        print(i+1,song)
