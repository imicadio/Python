# -*- encoding: utf8 -*-


# zwroc wieksza z liczb x i y
def wieksza(x,y):
    if x > y:
        return x
    elif x < y:
        return x
    else:
        return None


# zostaje w domu gdy pada deszcz lub gdy jest wieczór i mam gości
# Napisz funkcję zwracającą True/False w zależności od wartości argumentów (wartości logiczne)
def zostaje_w_domu(pada_deszcz, jest_wieczor, mam_gosci):
    if pada_deszcz or (jest_wieczor and mam_gosci):
        return True
    else:
        return False


# zwroc True jeżeli x jest liczba parzysta
def czy_parzysta(x):
    if x%2 == 0:
        return True
    else:
        return False


# sprawdź czy słowo jest palindromem (brzmi tak samo czytane od lewej do prawej i od prawej do lewej)
def palindrom(slowo):
    revstr = slowo[::-1]
    if slowo == revstr:
        return True
    else:
        return False


# Dla danej listy stringów ze slowami zwróć liczbę takich stringów, których długości wynosi 2 lub więcej
# i których pierwszy i ostatni znak jest taki sam.
def zliczanie_stringow(slowa):
    stringi = []
    for i in slowa:
        if len(i) >= 2 and i[0] == i[-1]:
            stringi.append(i)

    return len(stringi)



# zwróć True jeżeli w tablicu jest więcej liczb ujemnych niż nieujemnych
def wiecej_ujemnych(tablica):
    dodatnie = 0
    ujemne = 0
    for i in tablica:
        if i >= 0:
            dodatnie += 1
        else:
            ujemne += 1
    if ujemne > dodatnie:
        return True
    return False


# przepisuj liczby z tablicy wejsciowej do tablicy wyjsciowej
# gdy natrafisz na 14, nie przepisuj jej i zwroc tablice wyjsciową
def przepisz(tablica):
    tab = []
    for i in tablica:
        if i != 14:
            tab.append(i)
        else:
            break
    return tab



# Sprawdź czy wartości w tablicy są posortowanie od największych do najmniejszych
def czy_posortowane(tablica):
    heh = 0
    for i in range(len(tablica) - 1):
        if tablica[i] >= tablica[i+1]:
            heh += 1
        else:
            return False
    return True



# zwroc True gdy hasło jest bezpieczne, lub False w przeciwnym razie
# bezpieczne hasło zawiera min. 8 znaków, z czego min. 2 znaki alfanumeryczne(a-z),
# min. 2 cyfry, i min. 1 znak specjalny
def bezpieczne_haslo(haslo):
    znaki = "abcdefghijklmnouprstqwxyz"
    specjalne = '!@#$%^&*()'
    cyfry = "0987654321"
    ileZnakow = 0
    ileSpecjalne = 0
    ileCyfr = 0
    wszystko = []
    if len(haslo) >= 8:
        for i in haslo:
            if i in znaki:
                ileZnakow += 1
            if i in specjalne:
                ileSpecjalne += 1
            if i in cyfry:
                ileCyfr += 1
            wszystko.append(i)

        if (ileZnakow >= 2) and (ileCyfr >= 2) and (ileSpecjalne >= 1):
            return True
    return False


# zwróć wszystkie liczby w przedziale [start,koniec] podzielne przez 7
# nie będące wielokrotnością 5. Funkcja powinna zwrócić string zawierający
# te liczby, oddzielone przecinkiem (bez spacji), np.: "2002,2009,2016"
def podzielne_7_nie_5(start, koniec):
    liczby = ''
    for i in range(start, koniec+1):
        if i%7 == 0 and i%5 != 0:
            liczby += str(i)
            liczby += str(',')
    liczby = liczby[:-1]
    return liczby



# dla tablicy wejsciowej [a1, a2, .., aN] zwroc tablice 2 wymiarowa postaci:
# [[a1, a2, .., aN]
# [a2, .., aN, a1]
# ...
# [aN, ..., a1, a2]]
#
# Przykladowo, dla tablicy [1,2,3] zwróć tablicę [[1,2,3], [2,3,1], [3,1,2]]
def przesuniecia(tab):
    if tab == []:
        return []

    wynik = []
    tablica = []

    for i in range(0, len(tab)):
        if i == 0:
            tablica.append(tab)
        else:
            for a in range(0, len(tab)):
                if i-1 == a:
                    x = tablica[a][0]
                    y = tablica[a]
                    for c in y[1:]:
                        wynik.append(c)
                    wynik.append(x)
                    tablica.append(wynik)
                    wynik = []
                    break

    return tablica


# Z klawiatury usunięto wszystkie klawisze poza tymi, które są niezbędne do
# wpisania tekstu w tekst1. Napisz funkcję, która zwróci True jeżeli tekst w tekst2 da
# się również zapisać przy użyciu takiej wybrakowanej klawiatury. W przeciwnym
# razie zwróć False. Interesują nas tylko klawisze a-z, 0-9. Wielkość liter nie ma znaczenia.
# Przykładowo:
# wybrakowana_klawiatura('ma', 'mama') == True
# wybrakowana_klawiatura('ab', 'abc') == False
# wybrakowana_klawiatura('abc', 'ab') == True
# wybrakowana_klawiatura('ab', 'AB') == True
def wybrakowana_klawiatura(tekst1, tekst2):
    wystapienia1 = {}
    tekst11 = tekst1.lower()
    tekst22 = tekst2.lower()

    for znak in tekst11:
        if znak in wystapienia1:
            wystapienia1[znak] += 1
        else:
            wystapienia1[znak] = 1

    for znak in tekst22:
        if znak in wystapienia1:
            wystapienia1[znak] -= 1
        else:
            return False
    return True


    # for a in tekst2:
    #    if a.lower() not in tekst1.lower():
    #        return False
    # return True


# Na stole leżą stosy książek, na pozycji i znajduje się stos wysokości h_i, stosy te zapisano w
# postaci tablicy stosy = [h0, h1, ...]. Sprzątanie stołu polega na usuwaniu stosów od najwyższych
# do najniższych (po uprzątnięciu pozycji i, przyjmij że wysokość stosu w tym miejscu wynosi 0)
# W przypadku stosów o równej wysokości sprzątnięty zostanie ten o mniejszej pozycji
# Zwróć tablicę zawierającą kolejność sprzątanych pozycji.
# Przykładowo, stosy [5,1,2] będą sprzątnięte w kolejności [0, 2, 1]
def sprzatanie(stosy):
    stosik = []

    for i in stosy:
        stosik.append(i)

    slownik = {}
    lista = []

    for i in range(len(stosik)):
        a = max(stosik)
        slownik[a] = i
        stosik.remove(a)

    for a in stosy:
        lista.append(slownik[a])

    return lista


# Dana jest macierz w postaci tablicy 2-wymiarowej
# Zwróć wartość minimalną spośród sum wierszy i kolumn
def najmniejsza_suma(macierz):
    suma_wierszy = []

    slownik = {}

    ile = 0

    nw = 0
    nk = 0

    ile_kolumn = 0
    ile_wierszy = len(macierz)

    for i in macierz:
        ile_kolumn = len(i)
        break

    # Suma wierszy
    for i in range(ile_wierszy):
        suma_wierszy.append(sum(macierz[i]))
        for a in range(ile_kolumn):
            if a not in slownik:
                slownik[a] = macierz[i][a]
            else:
                slownik[a] += macierz[i][a]

    suma_kolumn = slownik.values()

    nk = min(suma_kolumn)
    nw = min(suma_wierszy)

    if nw > nk:
        return nk
    return nw

from stos import Stack

# W tablicy znajdują się wyrazy i cyfry. Przejdź kolejno przez elementy tablicy i:
# gdy napotkasz wyraz, to odłóż go na stos
# gdy napotkasz cyfrę to wykonaj działanie z zależności od wartości:
# 0 - sklej 2 wyrazy z wierzchołka stosu, wynik odłóż na stos
# 1 - pobierz wyraz z wierzchołka stosu, przekształć go na wielkie litery (podpowiedź: "abc".upper()), odłóż na stos
# 2 - pobierz wyraz ze stosu, usuń z niego ostatnią literę, wynik odłóż na stos
# zwróć zawartość stosu począwszy od elementu leżącego najbliżej wierzchołka stosu do tego leżącego najgłębiej
def stos_wyrazow(tablica):
    stos = Stack()
    liczby = [0, 1, 2]
    lista = []
    string = ''

    for i in tablica:
        if i in liczby:
            if i == 0:
                x = stos.pop()
                y = stos.pop()
                string += str(x + y)
                stos.push(string)
                string = ''

            if i == 1:
                x = stos.pop()
                stos.push(x.upper())

            if i == 2:
                x = stos.pop()
                stos.push(x[:-1])
        else:
            stos.push(i)

    while not stos.is_empty():
        a = stos.pop()
        lista.append(a)

    return lista


# Oblicz sumę elementów tablicy, przy czym elementem tablicy może być też tablica,
# w takim przypadku policz sumę używając rekurencji
# Przykładowo:
# suma tablicy z elementami [1, [2, 3], 4] wynosi 10
def suma_rekurencyjna(tablica):
    suma = 0
    for i in tablica:
        if isinstance(i, list) == True:
            suma += suma_rekurencyjna(i)
        if isinstance(i, list) == False:
            suma += i
    return suma


# W tablicy "cyfry" znajduja sie cyfry w przedziale [1..9], ktore ksiegowa wpisuje przy pomocy klawiatury
# numerycznej o następującym układzie:
# 789
# 456
# 123
# Ksiegowa rozpoczyna wpisywanie cyfr od cyfry[0] i wprowadza kolejne cyfry z tablicy 1 palcem. Palec przesuwa
# się tylko w pionie i w poziomie, z klawisza na klawisz. Oblicz jaką droge pokonuje palec ksiegowej
# przy wpisywaniu wszystkich liczb (przeskok z klawisza na klawisz to odległość = 1). Przykładowo dla:
# palec_ksiegowej([4, 7, 5]) droga ta wynosi z 1 (z klawisza 4 na klawisz 7) + 2 (z klawisza 7 na klawisz 5) = 4.
def palec_ksiegowej(cyfry):
    tab = [None] * 3
    for x in range(len(tab)):
        tab[x] = [None] * 3

    sekwencja = []

    # wspolrzedne palucha
    if cyfry[0] == 1:
        paluch_x = 0
        paluch_y = 0

    if cyfry[0] == 2:
        paluch_x = 0
        paluch_y = 1

    if cyfry[0] == 3:
        paluch_x = 0
        paluch_y = 2

    if cyfry[0] == 4:
        paluch_x = 1
        paluch_y = 0

    if cyfry[0] == 5:
        paluch_x = 1
        paluch_y = 1

    if cyfry[0] == 6:
        paluch_x = 1
        paluch_y = 2

    if cyfry[0] == 7:
        paluch_x = 2
        paluch_y = 0

    if cyfry[0] == 8:
        paluch_x = 2
        paluch_y = 1

    if cyfry[0] == 9:
        paluch_x = 2
        paluch_y = 2

    # przesuniecie palucha
    for i in range(1, len(cyfry)):
        if cyfry[i] == 1:
            x = 0
            y = 0

        if cyfry[i] == 2:
            x = 0
            y = 1

        if cyfry[i] == 3:
            x = 0
            y = 2

        if cyfry[i] == 4:
            x = 1
            y = 0

        if cyfry[i] == 5:
            x = 1
            y = 1

        if cyfry[i] == 6:
            x = 1
            y = 2

        if cyfry[i] == 7:
            x = 2
            y = 0

        if cyfry[i] == 8:
            x = 2
            y = 1

        if cyfry[i] == 9:
            x = 2
            y = 2

        while True:

            dx = x - paluch_x
            dy = y - paluch_y

            if dx > 0 and dy > 0:
                sekwencja.append('N')
                paluch_y += 1

            elif dx < 0 and dy > 0:
                sekwencja.append('N')
                paluch_y += 1

            elif dx == 0 and dy > 0:
                sekwencja.append('N')
                paluch_y += 1

            elif dx > 0 and dy == 0:
                sekwencja.append('E')
                paluch_x += 1

            elif dx < 0 and dy == 0:
                sekwencja.append('W')
                paluch_x -= 1

            elif dx == 0 and dy < 0:
                sekwencja.append('S')
                paluch_y -= 1

            elif dx < 0 and dy < 0:
                sekwencja.append('S')
                paluch_y -= 1

            elif dx > 0 and dy < 0:
                sekwencja.append('S')
                paluch_y -= 1

            else:
                break

    return len(sekwencja)