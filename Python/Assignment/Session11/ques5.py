def update_cart(cart, item, qty):
    cart[item]=qty   #this is to update the cart. Without this the changes wont be updated in the dict
    return cart

cart={
    "Pizza":2,
    "Burger":1,
    "Cheese":4
}

item = input("Enter Item: ")
qty = int(input("Enter quantity: "))
update_cart(cart,item,qty)        #function calling
print(update_cart(cart,item,qty))    #print updated function