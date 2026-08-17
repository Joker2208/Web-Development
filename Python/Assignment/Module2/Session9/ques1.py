# lst = [1,2,3,4,5]
# square = lambda lst:[x**2 for x in lst]
# print(square(lst))


squares = lambda x:x**2
for i in range(1,6):
    print(squares(i))
