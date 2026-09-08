from tkinter import *
import mysql.connector as sql

con = sql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "",
    database = "python"
)

cursor = con.cursor()

root = Tk()
root.geometry("500x500")
root.title("My App")

def data():
    name = t.get()
    email = t1.get()
    phone = t2.get()

qry = "create table student"

l = Label(root,text="Username:")
l.place(x=100,y=100)

l1 = Label(root,text="Email:")
l1.place(x=100,y=120)

l2 = Label(root,text="Phn no:")
l2.place(x=100,y=140)

t = Entry(root)
t.place(x=170,y=100)

t1 = Entry(root)
t1.place(x=170,y=120)

t2 = Entry(root)
t2.place(x=170,y=140)

b = Button(root,text="Submit")
b.place(x=170,y=180)


root.mainloop()
