class Influencer:
    def __init__(self,username,followers):
        self.username = username
        self.followers = followers

class Brand:
    def __init__(self,brand_name):
        self.brand_name = brand_name

class BrandPartner(Influencer,Brand):
    def __init__(self, username, followers,brand_name):
        super().__init__(username, followers)
        Brand.__init__(self,brand_name)

    def display(self):
        print(self.username,self.followers,self.brand_name)

b = BrandPartner("Dipesh",10000,"Livspace")
b.display()