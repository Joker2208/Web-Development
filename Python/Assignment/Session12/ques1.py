def get_discounted(price,percent):
    final = price - (price*percent)/100
    return final

price = float(input("Enter your amount: "))
percent = float(input("Enter discount: "))
print(get_discounted(price,percent))