wynik = 0

i = 0

while i < 3:
    x = int(input("Podaj dodatnią liczbę: "))
    if (x > 0):
        wynik += x
    else:
        print("Liczba nie jest dodatnia!")
        continue
    print("Aktualny wynik dodawania to: ", wynik)
    i += 1