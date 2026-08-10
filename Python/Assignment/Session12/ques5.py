prices= [120, 80, 150, 60]

from functools import reduce

total = reduce(lambda a,b:a+b,prices)
print(total)
