flag = "y"

while flag=="y":
    marks = int(input("Enter your marks: "))

    if marks >= 91 and marks <=100:
        print("Your grade is A")

    elif marks >= 71 and marks <=90:
        print("Your garde is B")

    elif marks >= 51 and marks <=70:
        print("Your grade is C")

    elif marks >=35 and marks <=50:
        print("Your grade is D")

    elif marks >=0 and marks <=34:
        print("Your grade is F")

    else:
        print("Invalid marks")

    flag = input("Do you want to continue? Press Y for yes or N for no:")

    if flag == "n":
        print("Bye Bye")
