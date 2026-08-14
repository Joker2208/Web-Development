scores= [56.7, 102.3, 88.9, 45.2, 120.8]
final = []

for i in range(len(scores)):
    rounded=round(scores[i])
    final.append(rounded)
print(final)