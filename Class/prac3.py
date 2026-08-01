bill = float(input("Enter your bill amount: "))
coupon = str(input("Enter coupon: "))


if bill > 100 and coupon == "PREMIUM15":
    print("You get a discount")

else:
    print("No discount for you.")