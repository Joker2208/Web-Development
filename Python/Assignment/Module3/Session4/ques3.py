class PaymentFailedError(Exception):
    pass

amount = int(input("Enter your amount:"))

def process_payment(amount):
    try:
        if amount <= 0:
            raise PaymentFailedError(amount)
        else:
            print("Payment Successful")
    except PaymentFailedError as p:
        print("Invalid amount",p)

process_payment(amount)