def book_movie_ticket(movie_name, seat_type='Regular', snacks=None):
    print(movie_name +" "+ seat_type +" "+( snacks if snacks else ""))

book_movie_ticket("Jawan")
book_movie_ticket(movie_name="Pathaan",seat_type="VIP")
book_movie_ticket("Pathaan",snacks="Samosa")


