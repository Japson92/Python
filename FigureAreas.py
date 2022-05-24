import math
from enum import IntEnum

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

def floatCheck(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

AreaMenu = IntEnum('AreaMenu', "Rectangle Square Triangle Trapeze Circle")

while True:
    print("Hello!")
    print(" 1 - Rectangle \n 2 - Square\n 3 - Triangle\n 4 - Trapeze\n 5 - Circle")
    chose = input("Chose which area You want to calculate! ")
    if chose.isdigit():
        chose = int(chose)
        if (chose == AreaMenu.Rectangle):
            while True:
                a = input("Insert size of first rectangle side: ")
                b = input("Insert size of second rectangle side: ")
                if floatCheck(a) and floatCheck(b):
                    a = float(a)
                    b = float(b)
                    print("Rectangle area is:", rectangleArea(a, b))
                    break
                else:
                    print("Your data is wrong!! Please insert numbers!!")
                    continue
        elif (chose == AreaMenu.Square):
            while True:
                a = input("Insert size of square side: ")
                if floatCheck(a):
                    a = float(a)
                    print("Square area is:", squareArea(a))
                    break
                else:
                    print("Your data is wrong!! Please insert numbers!!")
                    continue
        elif (chose == AreaMenu.Triangle):
            while True:
                a = input("Insert triangle bottom side size: ")
                h = input("Insert triangle height: ")
                if floatCheck(a) and floatCheck(h):
                    a = float(a)
                    h = float(h)
                    print("Triangle area is:", triangleArea(a, h))
                    break
                else:
                    print("Your data is wrong!! Please insert numbers!!")
                    continue
        elif (chose == AreaMenu.Trapeze):
            while True:
                a = input("Insert shorter side of trapeze: ")
                b = input("Insert longer side of trapeze: ")
                h = input("Insert trapeze height: ")
                if floatCheck(a) and floatCheck(b) and floatCheck(h):
                    a = float(a)
                    b = float(b)
                    h = float(h)
                    print("Trapeze area is:", trapezeArea(a, b, h))
                    break
                else:
                    print("Your data is wrong!! Please insert numbers!!")
                    continue
        elif (chose == AreaMenu.Circle):
            while True:
                r = input("Insert circle radius: ")
                if floatCheck(r):
                    r = float(r)
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
    else:
        print("You pick wrong number! Try again!")
        continue    