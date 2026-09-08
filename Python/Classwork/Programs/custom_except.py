class MyException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def check_age(age):
        if age>18:
            print("Adult")
        else:
            raise MyException("Kid")

try:
    check_age(10)
except MyException as e:
     print(e)    