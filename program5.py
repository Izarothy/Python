name = input("Wpisz swoje imię: ")
age = int(input("Wpisz swój wiek: "))
count = int(input("Ile kopii tej wiadmości chcesz?? "))
a = 0

yea = 100 - age
year = 2020 + yea

while a < count:
    print(name + ", będziesz miał 100 lat za " + str(year) + "!")
    a += 1
