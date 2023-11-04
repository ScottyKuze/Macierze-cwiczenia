A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
B = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
C = [[2, 1], [0, 1, 2], [1, 2, 3]]
D = [[0, 1, 2], [1, 2, 3]]
E = [[0, 2], [2, 0]]
F = [[1, 0], [0, 1]]

macierze = [A, B, C, D, E, F]


# sprawdza czy macierz jest kwadratowa
# kod zoptymalizowany - wykorzystanie len (length) i indeksów
def kwadratowa(macierz):
    liczba_wierszy = len(macierz)
    for i in range(0, len(macierz)):
        liczba_kolumn = len(macierz[i])
        if liczba_kolumn == liczba_wierszy:
            continue
        else:
            return False
    return True


# sprawdza czy jest jednostkowa
def jednostkowa(macierz):
    if not kwadratowa(macierz):
        return False
        # macierz niekwadratowa nie może być jednostkowa
    for i in range(0, len(macierz)):
        for j in range(0, len(macierz[i])):
            # przypadek gdy indeksy są te same (powinno być == 1)
            if i == j:
                if macierz[i][j] == 1:
                    continue
                else:
                    return False
            else:
                if macierz[i][j] == 0:
                    continue
                else:
                    return False
    return True


def print_macierz(macierz):
    for i in macierz:
        for j in i:
            print(j, end=" ")
        print("")  # bez tego rozpierdoli cały kod
    print(f"""
Czy jest kwadratowa: {kwadratowa(macierz)}
Czy jest jednostkowa: {jednostkowa(macierz)}

""")


for mac in macierze:
    print_macierz(mac)
