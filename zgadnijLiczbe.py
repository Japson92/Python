szukanaLiczba = 40

x = 0
i = 0
while x != szukanaLiczba:
    x = int(input("Sekretna liczba to: "))
    if x == szukanaLiczba:
        print("Brawo zgadłeś!!")
        i += 1
        break
    elif x < szukanaLiczba:
        print("Sekretna liczba jest wieksza")
        i += 1
    elif x > szukanaLiczba:
        print("Sekretna liczba jest mniejsza")
        i += 1
        

print("Liczba prób zgadnięcia to: ", i)