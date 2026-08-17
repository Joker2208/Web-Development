def apply_coupon(amount, coupon_code=None):
    print(amount-(amount * 0.10) if coupon_code == "SAVE10" else amount)

apply_coupon(100,"SAVE10")
apply_coupon(100)
