names = ['Burger Hub', 'Pizza Point', 'Sushi House']
minutes = [30, 25, 40]

for restaurant, delivery in zip(names,minutes):
    print(restaurant,"-",delivery,"min")