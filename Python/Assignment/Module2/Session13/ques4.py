users = [[4, 5, 3, 2], [5, 4, 4, 3], [3, 2, 5, 5]]

final = [x for rating in users for x in rating if x>4]
print(final)