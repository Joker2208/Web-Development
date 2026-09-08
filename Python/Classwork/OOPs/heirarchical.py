class Account():
    balance = 0
    def get_balance(self):
        print(f"Current balance is {self.balance}")

    def deposit(self,amount):
        pass

    def withdraw(self,amount):
        pass
        

class Savings(Account):
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient Balance")
        else:
            self.balance-=amount

class Loan(Account):
    def withdraw(self,amount):
        self.balance+=amount

    def deposit(self,amount):
        if amount > self.balance:
            k = amount-self.balance
            print(f"Loan cleared - Return amount is {k}")
        else:
            self.balance-=amount

s = Savings()
s.get_balance()
s.deposit(5000)
s.get_balance()
s.withdraw(2000)
s.get_balance()

l  = Loan()
l.get_balance()
l.withdraw(5000)
l.get_balance()
l.deposit(10000)
l.get_balance()

