class student:
    def __init__(self,id,name,email):
        self.id = id 
        self.name = name
        self.email = email

    def display(self):
        print(self.id,self.name,self.email)

s = student(10,"Dipesh","d@ymail.com")
s.display()

id = input("Enter id: ")
name = input("Enter name: ")
email = input("Enter email: ")
s=student(id,name,email)
s.display()