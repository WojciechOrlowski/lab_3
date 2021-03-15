# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x:x∈<1,10>}
# B = {1,4,16,…,47}
# C = {x:x∈B i x jest liczbą podzielną przez 2}

# liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# A = []
# for i in liczby:
#     A.append(1 - i)
# print(A)
#
# B = []
# for a in range(8):
#     B.append(4**a)
# print(B)
#
# C = []
# for m in range(8):
#     if m % 2 == 0:
#         C.append(4**m)
# print(C)
###########################################################################
# Zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1,
# następnie wykorzystując Python Comprehension zdefiniuj nową listę,
# która będzie zawierała tylko parzyste elementy

# lista1 = [random.randint(1, 27) for x in range(10)]
# lista2 = [x for x in lista1 if x % 2 == 0]
# print(lista1)
# print(lista2)
###########################################################################
# Zad3
# Utwórz słownik z produktami spożywczymi do kupienia.
# Klucz to niech będzie nazwa produktu a wartość -
# jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy,
# gdzie będą produkty, których wartość to sztuki.

# towary = {'bułki' : 'sztuk', 'ziemniaki' : 'kg', 'woda' : 'l'}
# ilosc = {}
# for key, a in towary.items():
#     if a == 'sztuk':
#         ilosc[a] = key
# print(ilosc)
###########################################################################
# Zad4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.

# def pitagoras(a, b, c):
#     if a > b and a > c:
#         if a ** 2 == b ** 2 + c ** 2:
#             return 'Trójkąt jest prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
#     elif b > a and b > c:
#         if b ** 2 == a ** 2 + c ** 2:
#             return 'Trójkąt jest prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
#     elif c > a and c > b:
#         if c ** 2 == a ** 2 + b ** 2:
#             return 'Trójkąt jest prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
###########################################################################
# Zad5
# Zdefiniuj funkcje która policzy pole trapezu.
# Funkcja ma przyjmować wartości domyślne.

# def poletrapezu(a = 1, b = 2, h = 3):
#     return ((a + b) * h / 2)
###########################################################################
# Zad6.
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa),
# b (wielkość o ile mnożone są kolejne elementy), ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10

# def ciag(a = 1, b = 4, ile = 10):
#     print(a)
#     for x in range(a, ile):
#         print(x * b)
# ciag()
###########################################################################
# Zad7
# Napisz funkcje za pomocą operatora *,
# która wykona te same działanie co w zadaniu 6.

# def ciag(*liczby):
#     if len(liczby) != 3:
#         print('Podaj trzy liczby!')
#         return -1
#     print(liczby[0])
#     for x in range(liczby[0], liczby[2]):
#         print(x * liczby[1])
#
# ciag(1, 2, 3)