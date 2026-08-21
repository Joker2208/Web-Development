wallet = 5000
def book_movie_ticket():
    try:
        tickets = int(input("Enter no. of tickets: "))
        price = wallet / tickets    
        print(price)
        
    except ZeroDivisionError:
        print("Cannot divide by Zero. Try again")
    except ValueError:
        print("Enter a number only..")


book_movie_ticket()
