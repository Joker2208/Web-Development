import math

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in ms: "))

square = math.pow(height,2)
bmi = weight/square
sq = round(bmi,2)
print(sq)