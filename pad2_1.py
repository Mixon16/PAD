print("Podaj liczbę: ")
liczba = int(input())
dodaj15 = lambda a: a+15
print(dodaj15(liczba))
print("Podaj x: ")
x = float(input())
print("Podaj y: ")
y = float(input())
iloczyn = lambda x,y: x*y
print("Iloczyn to: ", iloczyn(x,y))