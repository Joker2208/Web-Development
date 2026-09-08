# sub = ["python","node","java","php","android"]

# r = filter(lambda x : x.startswith('p'),sub) #use startwith string function
# print(list(r))

# x = filter(lambda y: "a" in y,sub)
# print(list(x))


l =[4,5,6,9,25,45,144,169,36,11,17,27]

r = filter(lambda a: a>=0 and int (a**0.5)**2 ==a,l)
print(list(r))