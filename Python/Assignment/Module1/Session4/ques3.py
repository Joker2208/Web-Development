age = int(input("Enter your age: "))
time = float(input("Enter current time in 24 hour format: "))

if age >= 18:

    if time >= 22 or time <= 2:
        print("You can order.")

else:
    print("You cannot order.")
