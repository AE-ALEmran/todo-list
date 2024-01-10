try :
    width=float(input("Enter the rectangle width : "))
    length=float(input("Enter the rectangle length : "))
    if width == length :
        exit("This is a Square .")
    Area = width*length
    print(Area)
except ValueError :
    print("Enter a Number .")