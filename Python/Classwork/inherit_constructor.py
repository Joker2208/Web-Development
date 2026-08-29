class Pen():
    def __init__(self,price,colour,company):
        self.price = price
        self.colour = colour
        self.company = company

    def display(self):
        print(self.price,self.colour,self.company)

class Pencil():
    def __init__(self,length):
        self.length = length

class Notebook(Pen):
    def __init__(self, price, colour, company,pages):
        self.pages =pages
        super().__init__(price, colour, company)

    def display(self):
        print(self.price,self.colour,self.company,self.pages)

p = Pen(50,"red","cello")
p.display()

n = Notebook(100,"White","Class mate",500)
n.display()