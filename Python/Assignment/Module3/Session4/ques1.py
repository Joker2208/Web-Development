#Create a custom exception class called InvalidCouponCodeError for a Zomato-style food ordering app, and raise this exception if a user tries to apply a coupon code that is not in the list of valid codes.



class InvalidCouponCodeError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

lst = ["BEN10","SUPER50"]
code = input("Enter coupon code:")

try:
    if code not in lst:
        raise InvalidCouponCodeError(code)
    else:
        print("Code Accepted.")
except InvalidCouponCodeError as I:
    print(I,"Invalid Code.")