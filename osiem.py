#coding=utf-8
import operator

# funkcja laczy 2 posortowane tablice left i right
# w jedna posortowana tablice wynikową
def merge(left, right, compare=operator.lt):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

print(merge_sort([10,4,2,8,3]))
print(merge_sort([10,-4,-2,-8,3]))

# W DOMU:
def sortuj_filmy(filmy):
    bez_the = []
    slownik = {}
    for i in filmy:
        film = i.lower()
        if len(film) < 5:
            bez_the.append(film)
        else:
            if film[0:4] == "the ":
                bez_the.append(film[4:])
            else:
                bez_the.append(film)
    for a in range(len(filmy)):
        slownik.update({bez_the[a]:filmy[a]})

    lista = merge_sort(list(slownik.keys()))
    result = []
    for x in lista:
        result.append(slownik[x])
    return result

print(sortuj_filmy(['The Road', 'The Accountant', 'Alladin', 'Bad Boys', 'Zorro', 'Terminator']))

def zmiana(f,od=0,do=None):
    if do is None:
        do = len(f)-1

    if f[od] > 0 and f[do] > 0:
        return None
    if f[od] < 0 and f[do] < 0:
        return None

    if f[od] <= 0 and f[do] > 0:
        if od == do-1 or f[od] == 0:
            return od
        srodek = (od + do) // 2
        if f[srodek] == 0:
            return srodek
        a = zmiana(f,od,srodek)
        if a is not None:
            return a
        return zmiana(f,srodek,do)

print(zmiana([-10,-7,-6,-3,-1,3,5,6]))