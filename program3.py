while True:
    n = int(input("Podaj liczbę, którą chcesz rozłożyć na czynniki: "))
    if (n < 10**9):
        m = n

        while m >= 1:
            if (n % m) == 0:
                i = (n / m)
                print (int(i))
                m -= 1
            elif (n % m) != 0:
                m -= 1
    elif (n >= 10**9):
        print("Liczba jest za duża!")

input()