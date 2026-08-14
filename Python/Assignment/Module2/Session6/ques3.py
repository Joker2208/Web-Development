ipl = ["GT","RCB","MI","CSK"]
table = [10,24,19,3]

dict1 = dict(zip(ipl,table))

for team,points in dict1.items():
    if points > 10:
        print(f"{team}{points}")
    