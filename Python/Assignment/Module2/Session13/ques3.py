names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

join = [(x,y )for x,y in zip(names,prices) if y>1000]
print(join)