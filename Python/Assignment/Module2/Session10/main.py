from playlist import *

new = []

new = add_song("Kesariya",new)
new = add_song("Shape of you",new)
new = add_song("Believer",new)
print(new)

new = remove_song("Shape of you",new)
print(new)


new = display_playlist(new)