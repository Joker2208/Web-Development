try:
    price = float(input('Enter price: '))     #this needs to be inside the try block depending on the problem in this case the error needs to be printed when a number is not inputed if put outside try block the data type error will occur and will fail the purpose of try and except



    qty = int(input("Enter qty: "))   #same with this as well
    total = price * qty
    print(f"Your total is {total}")
except ValueError:
    print("Error. Only numbers.")