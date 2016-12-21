def kwadrat(a, b, c):
    if b/c == 1/2 or b/c == 1 or b/c == 2:
        return False

    if a <= b + c:
        return False

    tab = [None] * 3
    for x in range(len(tab)):
        tab[x] = [None] * 3

    for i in range(len(tab)):
        if i == 0:
            for y in range(len(tab)):
                if y == 0:
                    e = a-b
                    tab[i][y] = e

                if y == 1:
                    e = a + b - c
                    tab[i][y] = e

                if y == 2:
                    e = a + c
                    tab[i][y] = e

        if i == 1:
            for y in range(len(tab)):
                if y == 0:
                    e = a + b + c
                    tab[i][y] = e

                if y == 1:
                    tab[i][y] = a

                if y == 2:
                    e = a - b - c
                    tab[i][y] = e

        if i == 2:
            for y in range(len(tab)):
                if y == 0:
                    e = a - c
                    tab[i][y] = e

                if y == 1:
                    e = a - b + c
                    tab[i][y] = e

                if y == 2:
                    e = a + b
                    tab[i][y] = e


    return tab




print(kwadrat(5, 3, 1))
