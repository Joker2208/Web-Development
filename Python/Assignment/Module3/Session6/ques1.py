class User:
    
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def display(self):
        print(f"Username is {self.username} and email is {self.email}")

u = User("Dipesh","d@gmail.com")
u.display()
