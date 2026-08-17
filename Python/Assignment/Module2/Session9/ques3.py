users = [('raj', 800), ('simran', 1500), ('veer', 1200), ('ananya', 950)]
names = [x[0] for x in filter(lambda x: x[1]>=1000,users)]
print(names)