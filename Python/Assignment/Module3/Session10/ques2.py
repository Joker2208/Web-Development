from tkinter import *

root = Tk()
root.title('My Playlist')

label = Label(root, text='Welcome to Your Music Playlist')
label.pack()
root.geometry("400x300")

def play():
    status_label.config(text='Playing')

def pause():
    status_label.config(text='Paused')

def next_song():
    status_label.config(text='Next Song')

play_button = Button(root, text='Play', command=play)
pause_button = Button(root, text='Pause', command=pause)
next_button = Button(root, text='Next', command=next_song)

play_button.pack()
pause_button.pack()
next_button.pack()

status_label = Label(root, text='Status')
status_label.pack()
root.mainloop()