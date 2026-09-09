from tkinter import *

root = Tk()
root.title('Login Form')
root.geometry("300x200")

username_label = Label(root, text='Username')
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

password_label = Label(root, text='Password')
password_label.pack()
password_entry = Entry(root, show='*')
password_entry.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        result_label.config(text='Login Successful')

login_button = Button(root, text='Login', command=login)
login_button.pack()

result_label = Label(root, text='')
result_label.pack()

root.mainloop()