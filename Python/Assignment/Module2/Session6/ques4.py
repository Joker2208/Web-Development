titles = ["Spiderman","Openheimer","Interstellar"]
genres = ["Superhero","History","Sci-fi"]
ratings = [7.5,8.6,9.8]

dict1 = [{"title":t,"genre":g,"rating":r} for t,g,r in zip(titles,genres,ratings)]
print(dict1)