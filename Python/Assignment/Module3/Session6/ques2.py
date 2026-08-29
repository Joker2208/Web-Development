class User:
    def __init__(self,username):
        self.username = username

class Influencer(User):
    def __init__(self,username,followers):
        super().__init__(username)
        self.followers = followers

    def display(self):
        print(self.username,self.followers)

i = Influencer("Dipesh",100)
i.display()
