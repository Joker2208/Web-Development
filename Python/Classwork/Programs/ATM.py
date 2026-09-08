curr_bal = 5000

choice = 0

while choice != 4:
    print("\n--- ATM Menu ---")
    print("1. View current balance")
    print("2. Withdrawal")
    print("3. Deposit")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Your current available balance is: ",curr_bal)
        
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > curr_bal:
            print("Insufficient balance!")
        else:
            curr_bal -= amount
            print("Amount withdrawn successfully. Remaining balance: ",curr_bal)
    
    elif choice == 3:
        amount = int(input("Enter the amount you want to deposit:"))
        amount += curr_bal
        print("Your current balance is:", amount)

    elif choice == 4:
        print("Thank you for your business.")

    else:
        print("Invalid choice")
