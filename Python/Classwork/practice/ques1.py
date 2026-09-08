# Lists, Tuples & Dicts

# Take a list of 10 numbers and separate them into two new lists: evens and odds. Hint: loop + modulo, append conditionally.

    # lst = [1,2,3,4,5,6,7,8,9,10]
    # even = []          #[x for x in lst if x%2==0]     
    # odd = []         #[x for x in lst if x%2==1]

    # for i in lst:
    #     if i%2==0:
    #         even.append(i)
    #     else:
    #         odd.append(i)

    # print(even)
    # print(odd)



# Given a list with duplicate values, remove duplicates while preserving the original order. Hint: a list + a "seen" check, or dict.fromkeys().

                # lst = [1,1,2,3,4,5,4,6]

                # k = dict.fromkeys(lst)
                # print(list(k))


# Swap the first and last elements of a list without using a temp variable. Hint: tuple unpacking works on indices too.

# lst = [1,2,3,4,5]
# a = lst[0]
# b = lst[-1]
# lst[0] = b
# lst[-1] = a
# print(lst)


# Store 5 students' names and marks as a list of tuples, then sort by marks descending. Hint: sorted() + lambda + reverse.

# students = [("Dipesh",10),("Hasib",50),("Purv",100),("Alama",67),("asxbnd",78)]
# marks = sorted(students, key= lambda x:x[1], reverse =True)
# print(marks)



# Given two dictionaries, merge them into one — if a key exists in both, sum their values. 

    # gradeA = {
    #     "Dipesh":100,
    #     "Rutu":99,
    #     "Mia":69
    # }

    # gradeB = {
    #     "Dipesh":87,
    #     "Rutu":100,
    #     "Autumn":20
    # }

    # result=gradeA.copy()

    # for key,value in gradeB.items():
    #     result[key] = result.get(key,0) + value

    # print(result)


# Functions & Lambda
# 6. Write a function that accepts any number of numbers and returns their average. Hint: args + sum()/len().

def avg():


# 7. Write a function with a default parameter for tax rate, and use it to calculate a bill total. Hint: def calc(amount, tax=0.18).
# 8. Use a lambda with filter() to get only strings longer than 4 characters from a list. Hint: filter(lambda, list) returns an iterator — wrap in list().
# 9. Use map() with a lambda to convert a list of Celsius temperatures to Fahrenheit. Hint: F = C9/5 + 32.
# 10. Write a function that takes a dictionary of employee:salary and returns the name of the highest-paid employee — without using max() directly. Hint: manual loop, track a running "best so far".

# Comprehensions
# 11. Use a list comprehension to get all vowels from a given sentence.
# 12. Use a dictionary comprehension to map each word in a sentence to its length.
# 13. Use a nested list comprehension to build a 3x3 multiplication table as a list of lists.
# 14. Given a list of dicts (each with 'name' and 'score'), use a comprehension to build a list of only the names where score > 50.

# File Handling
# 15. Write a program that writes 5 lines of user input to a file, then reads and prints them back.
# 16. Count how many lines a text file has, without loading readlines() into memory — using a loop.
# 17. Write a program that appends a new "log entry" (with a message) to a file every time it runs, without erasing old entries.
# 18. Read a file and count how many times a specific word appears in it, case-insensitively.
# 19. Write a program that copies content from one file to another using file handling only (no shutil).

# Exception Handling
# 20. Write a calculator that takes two numbers and an operator (+,-,*,/) from the user and handles divide-by-zero and invalid operator input separately.
# 21. Write a program that keeps asking the user for a number until valid integer input is given, using try-except in a loop.
# 22. Create a custom exception NegativeAmountError and raise it if a deposit amount entered by a user is negative.
# 23. Write a function that opens a file and handles the case where the file doesn't exist, printing a friendly message instead of crashing.
# 24. Write a program with try-except-else-finally that reads a number from a file, doubles it, and always prints "Operation attempted" in finally.

# OOP Basics
# 25. Create a Student class with name and marks; add a method is_pass() that returns True if marks >= 40.
# 26. Create a BankAccount class with deposit() and withdraw() methods; withdraw() should raise an exception if balance is insufficient.
# 27. Create a class Rectangle with length and breadth; add methods for area() and perimeter().
# 28. Create a class where one attribute is private (using __) and add a getter method to access it safely.
# 29. Create a Book class and override the __str__ method so printing a Book object shows "Title by Author" instead of a memory address.

# Inheritance
# 30. Create a base class Employee and a subclass Manager that adds a bonus attribute — calculate total salary in the subclass.
# 31. Create a 3-level inheritance chain: Vehicle → Car → ElectricCar, each adding one new attribute.
# 32. Create two classes Teacher and Student that both inherit from a common Person class with shared attributes name/age.
# 33. In a subclass, override the parent's __init__ but still call the parent's version using super().

# Polymorphism / Overriding
# 34. Create a Shape base class with an area() method, and Circle/Rectangle subclasses that override it — loop through a list of shapes and print each area.
# 35. Write two unrelated classes (no shared parent) that both have a make_sound() method, then call it on both using the same loop — demonstrate duck typing.
# 36. Simulate method overloading in Python (since it's not natively supported) by writing one method that behaves differently based on number of arguments passed.
# 37. Create a Payment class with a pay() method, and subclasses CardPayment/UpiPayment that override it with different print messages.

# Modules & Packages
# 38. Create your own module calculator.py with add/subtract/multiply/divide functions, then import and use it in a separate main file.
# 39. Create a small package with two modules inside it (e.g., shapes.py and utils.py), with a proper __init__.py, and import functions from both into a main script.
# 40. Use the random module to build a simple number-guessing game (generate a random number, let the user guess with attempts counted).

# Regex
# 41. Write a program using re to validate whether a given string is a valid email address.
# 42. Extract all phone numbers (10-digit) from a block of text using re.findall().
# 43. Use re.sub() to replace all digits in a string with #.

# Tkinter
# 44. Build a simple Tkinter GUI with an entry box and a button — clicking the button should show the entered text in a label.
# 45. Build a basic Tkinter calculator with buttons for +, -, *, / and two entry fields.
# 46. Build a Tkinter form with Name and Age fields, and a "Submit" button that prints the values to console.

# Database (pymysql)
# 47. Connect to a MySQL database and insert a new student record (name, marks) into a students table using pymysql.
# 48. Write a program that connects to MySQL, fetches all records from a students table, and prints only those with marks above 60.

# Integrative (mixed, tricky, exactly how interviewers combine topics)
# 49. Build a small "Library System": a Book class (OOP), store multiple books in a list of objects, write all book titles to a file (file handling), and wrap the whole thing in try-except in case the file write fails.
# 50. Build an "Employee Management" mini-project: a class Employee with name/salary, store several employees in a dictionary, use a lambda + sorted() to rank them by salary, and use regex to validate that each employee's ID follows a pattern like EMP001.



