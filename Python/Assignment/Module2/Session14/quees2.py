def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    if user not in playlists:
        playlists[user] = {}

    playlists[user][playlist_name].append(song_title)
    return playlists