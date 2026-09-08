from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("My App")

# b = Button(root,text="Submit")
# b.pack(side = LEFT)

# b1 = Button(root,text="Submit")
# b1.pack(side = RIGHT)

# b2= Button(root,text="Submit")
# b2.pack(side = TOP)

# b3 = Button(root,text="Submit")
# b3.pack(side = BOTTOM)

l = Label(root,text="Username")
l.grid(row = 1,column = 1)

l1 = Label(root,text="Email")
l1.grid(row = 2,column = 1)

l2 = Label(root,text="Phn no")
l2.grid(row = 3,column = 1)

t = Entry(root)
t.grid(row=1,column=2)

t1 = Entry(root)
t1.grid(row=2,column=2)

t2 = Entry(root)
t2.grid(row=3,column=2)

b = Button(root,text="Submit")
b.grid(row = 4,column = 2)


root.mainloop()
