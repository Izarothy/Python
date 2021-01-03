while True:
        dane = [input("Pierwsza liczba: "), input("Druga liczba: "), input("Trzecia liczba: ")]
        a = int(dane[0])
        b = int(dane[1])
        c = int(dane[2])

        if (1 < a and b and c < 1000000000):

            if (dane[0] + dane[1] > dane[2]):
                print("TAK")
            if (dane[0] + dane[1] < dane[2]):
                print ("NIE")
            if (dane[0] + dane[1] == dane[2]):
                print ("NIE")
        elif (1 < a, b, c > 1000000000):
            print ("Liczba jest za duża!")
        else:
            print("Liczba jest nieprawidłowa!")