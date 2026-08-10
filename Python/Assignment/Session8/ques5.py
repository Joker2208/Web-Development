def mask_phone_number(phone):
    star = "*" * 6
    digit = phone[-4:]
    final = star + digit 

    return final

phone = input("Enter a phone number: ")
print(mask_phone_number(phone))