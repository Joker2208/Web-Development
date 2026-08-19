import math

bill = float(input("Enter your bill amount: "))
discount = int(input("Enter discount: "))
disc = bill * (discount / 100)
final = bill - disc
print(math.floor(final))