import re

def is_valid_pnr(pnr):
    if re.match(r"^\d{10}$", pnr):
        return True
    else:
        return False

print(is_valid_pnr("1234567890"))   
print(is_valid_pnr("12345"))     
print(is_valid_pnr("12345abcde"))