val1 = float(input("Enter your 1st value:"))
val2 = float(input("Enter your 2nd value:"))
opr = input("Enter your desired operation:")

if opr == "+":
    print("Addition is:", val1 + val2)

elif opr == "-":
    print("Substraction is:", val1 - val2)

elif opr == "*":
    print("Multiplication is:", val1 * val2)

elif opr == "/":
    print("Division is:", val1 / val2)

elif opr == "%":
    print("Remainder is:", val1 % val2)

else:
    print("Invalid Operator.")
