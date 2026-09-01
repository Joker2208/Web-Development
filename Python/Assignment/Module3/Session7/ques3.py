class ZomatoOrder:
    def add_item(self,item,quantity=1):  #method overloading using default args
        self.item = item
        self.quamntity = quantity
        print(f"{item} : {quantity}")

z= ZomatoOrder()
z.add_item("Pizza")  #without giving the quantity it will still work because of the default value given in parameter up top

z.add_item("Pizza",2)
