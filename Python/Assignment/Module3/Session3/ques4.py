try:
    my_list = [1, 2, 3]
    print(my_list[5])
  
except IndexError:
    print("Wrong Index.")

try:
    my_dict = {'a': 1}
    print(my_dict['b'])
    
except KeyError:
    print('Wrong key.')