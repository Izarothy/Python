while True:
    try:
        liczba = int(input("Wpisz liczbę, która będzie parzysta lub nieparzysta: "))

        if liczba % 2 == 0 or 1:
            podzielnosc = liczba % 2

            if podzielnosc == 0 and liczba % 4 == 0:
                print("Liczba jest parzysta i podzielna przez 4!")
            elif podzielnosc == 0:
                print("Liczba jest parzysta!")
            elif podzielnosc == 1:
                print("Liczba jest nieparzysta!")
        else:
            print("Podałeś błędną wartość!")
        num = int(input("Podaj pierwszą liczbę: "))
        check = int(input("Podaj drugą liczbę: "))

        if num % check == 0:
            print("Dzielą się bez reszty!")
        else:
            print("Dzielą się z resztą.")
    except ValueError:
        print("Podałeś błędną wartość!")

