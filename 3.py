a = int(input())
b = int(input())
c = int(input())
d = int(input())


def nod(a, b):
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return nod(a - b, b)
    else:
        return nod(a, b - a)


print(nod(nod(a, b), nod(c, d)))
