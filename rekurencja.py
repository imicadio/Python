wynik = []
def tablice(listy):
    for i in listy:
        if isinstance(i,list):
            wynik.append(tablice(i))
            wynik.pop()
        else:
            wynik.append(i)
    return wynik

print(tablice([1, [2, 3], [4, [5, 6, [7, 88]]]]))