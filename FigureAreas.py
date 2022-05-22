import math

def rectangleArea(a, b):
    return a * b

def squareArea(a):
    return a * a

def triangleArea(a, h):
    return 0.5 * a * h

def trapezeArea(a, b, h):
    return (a + b) / 2 * h 

def circleArea(r):
    return math.pi * r ** 2


while True:
    print("Hello!")
    print(" 1 - Rectangle \n 2 - Square\n 3 - Triangle\n 4 - Trapeze\n 5 - Circle")
    x = input("Chose which area You want to calculate! ")
    if x == "1":
        while True:
            a = input("Insert size of first rectangle side: ")
            b = input("Insert size of second rectangle side: ")
            if a.isdigit() and b.isdigit():
                a = int(a)
                b = int(b)
                print("Rectangle area is:", rectangleArea(a, b))
                break
            else:
                print("Your data is wrong!! Please insert numbers!!")
                continue
    elif x == "2":
        while True:
            a = input("Insert size of square side: ")
            if a.isdigit():
                a = int(a)
                print("Square area is:", squareArea(a))
                break
            else:
                print("Your data is wrong!! Please insert numbers!!")
                continue
    elif x == "3":
        while True:
            a = input("Insert triangle bottom side size: ")
            h = input("Insert triangle height: ")
            if a.isdigit() and h.isdigit():
                a = int(a)
                h = int(h)
                print("Triangle area is:", triangleArea(a, h))
                break
            else:
                print("Your data is wrong!! Please insert numbers!!")
                continue
    elif x == "4":
        while True:
            a = input("Insert shorter side of trapeze: ")
            b = input("Insert longer side of trapeze: ")
            h = input("Insert trapeze height: ")
            if a.isdigit() and b.isdigit() and h.isdigit():
                a = int(a)
                b = int(b)
                h = int(h)
                print("Trapeze area is:", trapezeArea(a, b, h))
                break
            else:
                print("Your data is wrong!! Please insert numbers!!")
                continue
    elif x == "5":
        while True:
            r = input("Insert circle radius: ")
            if r.isdigit():
                r = int(r)
                print("Rectangle area is:", circleArea(r))
                break
            else:
                print("Your data is wrong!! Please insert numbers!!")
                continue
    else:
        print("You pick wrong number! Try again!")
        continue
    chose = input("Do you want calculate another Area?(Yes/No) ").capitalize()
    if chose == "Yes":
        continue
    else:
        print("Good Bye!!")
        break
        