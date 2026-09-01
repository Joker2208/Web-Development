class Payment:
    def pay(self,amount):
        self.amount = amount
        print(f"Paying {amount}")

class UPI(Payment):
    def pay(self,amount):
        print(f"Paying {amount} via UPI")

p = Payment()
p.pay(100)
u = UPI()
u.pay(100)

