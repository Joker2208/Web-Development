def reverse_message(message):
    st = ""
    for ch in message:
        st=ch+st
    return st

message = str(input("Enter something: "))
print(reverse_message(message))