class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self, other):                           #this is inbuilt function if you want + to perfrom in different way. The name needs to stay the same or else it will be considered as a regular func and the overloading wont work

        return self.a+other.b,self.b+other.a            #Operator Overlaoding 

    def __mul__(self, other):           #same thing as the other one but for multiplication

        return self.a*other.a,self.b*other.b

    

c = Calc(10,20)
c1 = Calc(10,20)

r = c+c1
s= c*c1
print(r)
print(s)