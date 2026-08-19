duration = [[210, 180, 240], [150, 200], [300, 120, 90]]

final = [x for time in duration for x in time if x>200]
print(final)