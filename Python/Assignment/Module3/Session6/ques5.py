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

    @staticmethod
    def count(followers):
        if followers >= 1000000:
            followers /= 1000000
            return f'{followers}M'
        elif followers >=1000:
            followers /= 1000
            return f"{followers}K"
        else:
            return followers

    def display(self):
        print(self.username,self.count(self.followers),self.badge)

v = VerifiedInfluencer("Dipesh",1000000,"Verified")
v.display()

                                            