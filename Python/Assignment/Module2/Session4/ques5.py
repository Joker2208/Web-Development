duration = (23.567,12.5,4.3,4.675,3.67,8.98,2.10)
lst = list(duration)

final = [x for x in lst if x >= 5]
print(tuple(final))