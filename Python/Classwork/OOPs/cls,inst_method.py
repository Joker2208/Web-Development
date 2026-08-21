class User:
    college = "BMH"
    def __init__(self,name,email):    #this is a constructor
        self.name = name
        self.email = email

    def run(self):
        print(self.name,self.email,self.college)

    @classmethod
    def display(cls):        #use cls for class method as its naming convention
        print(cls.college)

    @staticmethod
    def sample():
        print("Static method")

User.college = "Gandhi"     #this shows that you can chng the value in the class anywhere

u = User("Dipesh","d@gmail.com")
u.run()

u = User("Rutu","r@gmail.com")
u.run()

User.display()
User.sample()