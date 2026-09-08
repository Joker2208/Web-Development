def test():
    try:
        k = int(input("Enter a number: "))
        return k
    except Exception as a:
        return a
    finally:
        print("Always Executes")

print(test())

