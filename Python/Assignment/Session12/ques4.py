devices =  ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

product = filter(lambda a:a.startswith("M"),devices)
print(list(product))