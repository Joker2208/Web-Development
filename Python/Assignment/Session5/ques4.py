song = str(input("Enter a song name: "))

for char in song:
    char= char.lower()
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print(char)
    else:
        pass