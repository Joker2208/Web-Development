num1 = float(input("Enter a number: "))
num2 =  float(input("Enter another number: "))

print("""Press 1 for Addition
      Press 2 for Substraction
      Press 3 for Multiplication
      Press 4 for Division
      Press 5 for modulo""")

choice = int(input("Enter your choice: "))

match(choice):
    case 1: print("Addition is: ",num1 + num2)
    case 2: print("Substraction is: ",num1 - num2)
    case 3: print("Multiplication is: ",num1 * num2)
    case 4: print("Division is: ",num1 / num2)
    case 5: print("Remainder is: ",num1 % num2)
    case _: print("Invalid Entry")