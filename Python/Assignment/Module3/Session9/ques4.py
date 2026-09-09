import re
lst = ['ORD1234', 'ORD5678', 'ORD9999', 'ORD0001']

for i in lst:
    order = re.match("ORD\d*[02468]$",i)
    if order:
        print(i)
    else:
        pass