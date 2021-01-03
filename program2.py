while True:
    try:
        t = int(input("Podaj liczbę całkowitą oznaczającą liczbę sekund: "))
        m = 0 
        s = 0

        if (t == 60):
            print ("Czas w odpowiednim formacie to 1m")
        if (t >=3600):
            g = t / 3600
            t = t % 3600

            if (t >= 60):
                m = t / 60
                t = t % 60
            if (t < 60):
                m = 0
            if (t >= 1):
                s = t

            print ("Czas w odpowiednim formacie to: " + str(int(g)) + "g" + str(int(m)) + "m"+ str(int(s)) +"s")
        elif (t >= 60 and t < 3600):
                m = t / 60
                t = t % 60

                if (t >= 1 and t < 60):
                    s = t
                    print ("Czas w odpowiednim formacie to: " + str(int(m)) + "m"+ str(int(s)) +"s")

        elif (t >=1 and t <60):
            print ("Podałeś liczbę mniejszą od minuty!")
        else:
            print ("Podałeś błędną liczbę!")
    except ValueError:
        print("Błędna wartość!")
input()