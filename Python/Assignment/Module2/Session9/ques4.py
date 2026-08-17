lst = [(3,4), (5,2), (7,8)]
cal = lambda x,y:(x+y, x*y)
for i,j in lst:
    final=cal(i,j)
    print(final)
