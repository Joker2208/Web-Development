class FoodOrder:
    def __init__(self,restaurant,items,price):
        self.restaurant = restaurant
        self.items = items
        self.price = price

    def show_order(self):
        print("Restaurant:",self.restaurant,",","Items:",self.items,",","Bill:",self.price)


f = FoodOrder("Cucina Marinara",["Pesto pizza","Vodka Pasta","Tiramisu"],3500)
f.show_order()