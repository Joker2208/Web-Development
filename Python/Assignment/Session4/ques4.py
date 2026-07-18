# Write a Python program that takes your favorite cricket team's score as input and prints a message: if score is 200 or more, print 'High Score!', if between 150 and 199, print 'Good Score', if between 100 and 149, print 'Average', else print 'Needs Improvement'. Use if, elif, else.

score = int(input("Enter the score: "))

if score >= 200:
    print("High Score!")

elif score >= 150 and score <= 199:
    print("Good Score")

elif score >= 100 and score <= 149:
    print("Average Score")

else:
    print("Needs Improvement")