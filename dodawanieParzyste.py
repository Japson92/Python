wynik = 0
i = 0

while (i < 3):
    x = int(input("Podaj liczbę parzystą dodatnią: "))
    if (x % 2 == 0 and x > 0):
        wynik += x
        i += 1
    else:
        print("Liczba jest nieparzysta lub ujemna!")

print("Suma liczb parzystych wynosi: ", wynik)