def square(a):
    for i in range(1,a):
        yield i*i   #you have to use yeild to make a generator

k = square(5)

for i in range(5):
    print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
