liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kwadraty = lambda liczby:[liczba**2 for liczba in liczby]
szesciany = lambda liczby:[liczba**3 for liczba in liczby]
print(F'kwadraty: {kwadraty(liczby)}')
print(F'sześciany: {szesciany(liczby)}')