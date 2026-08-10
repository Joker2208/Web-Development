food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}

items = food_order.keys()
print(items)
print()

quantity = food_order.values()
print(quantity)
print()

for item,quantity in food_order.items():
    print(item,quantity)