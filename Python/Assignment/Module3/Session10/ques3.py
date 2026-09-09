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

button_frame = Frame(root)
button_frame.pack()

button1 = Button(button_frame, text='Like')
button2 = Button(button_frame, text='Share')
button3 = Button(button_frame, text='Download')
button4 = Button(button_frame, text='Add to Queue')

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)

root.mainloop()