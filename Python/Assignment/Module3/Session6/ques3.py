class User:
    def __init__(self,username):
        self.username = username

class Influencer(User):
    def __init__(self, username,followers):
        super().__init__(username)
        self.followers = followers

class VerifiedInfluencer(Influencer):
    def __init__(self, username,followers,badge):
        super().__init__(username,followers)
        self.badge = badge

    def display(self):
        print(self.username,self.followers,self.badge)

v = VerifiedInfluencer("Dipesh",100,"Verified")
v.display()

    