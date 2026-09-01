class Content:
    def display(self, title):
        print('Title:', title)

class Movie(Content):
    def display(self, title, year):
        print("Title:",title," Year:",year)

m = Movie()
m.display("Interstellar",2016)