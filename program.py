import itertools

while True:
    
    x = int(input("Pierwsza wartość: "))
    y = int(input("Druga wartość: "))
    if (0 < x < y < 10000): 

        z = range(x, y+1)
        n = 0 
        for comb in itertools.combinations(z, 3):
          
         if (comb[0] + comb[1] > comb[2]):
            n+=1

        print("Liczba możliwych kombinacji z podanych wartości to: " + str(n) + "!")
        print("==========================")
    else:
     print("Podałeś błędne wartości!")
     print("==========================")

input()