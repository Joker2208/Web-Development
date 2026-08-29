print("Pattern Menu")
print("1. Hollow Square")
print("2. Hollow Rectangle")
print("3. Left C")
print("4. Right C")
print("5. U Pattern")
print("6. L Pattern")
print("7. Hollow Triangle")
print("8. Hollow Inverted Triangle")
print("9. Hollow Pyramid")
print("10. Hollow Inverted Pyramid")
print("11. Hollow Diamond")
print("12. Hollow Hourglass")
print("13. Hollow Butterfly")
print("14. Hollow X")
print("15. Hollow Plus")
print("16. Hollow Rhombus")
print("17. Hollow Parallelogram")
print("18. Hollow Arrow")
print("19. Hollow Kite")
print("20. Hollow Circle")

choice = int(input("Enter your choice (1-20): "))

match choice:
    case 1:
        # Hollow Square
        n = int(input("Enter size (n): "))
        for i in range(n):
            for j in range(n):
                if i == 0 or j==0 or i == n-1 or j == n-1:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()

    case 2:
        # Hollow Rectangle
        rows = int(input("Enter rows: "))
        cols = int(input("Enter cols: "))
        for i in range(rows):
            for j in range(cols):
                if  i == 0 or i==rows-1 or j ==0 or j == cols-1:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()

    case 3:
        # Left C
        pass

    case 4:
        # Right C
        pass

    case 5:
        # U Pattern
        pass

    case 6:
        # L Pattern
        pass

    case 7:
        # Hollow Triangle
        pass

    case 8:
        # Hollow Inverted Triangle
        pass

    case 9:
        # Hollow Pyramid
        pass

    case 10:
        # Hollow Inverted Pyramid
        pass

    case 11:
        # Hollow Diamond
        pass

    case 12:
        # Hollow Hourglass
        pass

    case 13:
        # Hollow Butterfly
        pass

    case 14:
        # Hollow X
        pass

    case 15:
        # Hollow Plus
        pass

    case 16:
        # Hollow Rhombus
        pass

    case 17:
        # Hollow Parallelogram
        pass

    case 18:
        # Hollow Arrow
        pass

    case 19:
        # Hollow Kite
        pass

    case 20:
        # Hollow Circle
        pass

    case _:
        print("Invalid choice")