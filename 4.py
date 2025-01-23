a = int(input())
b = int(input())
c = int(input())

def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def nok(a, b):
    return (a * b) // nod(a, b)

def nok_three(a,b,c):
    return nok(nok(a,b),c)

if a > 0 and b > 0 and c > 0:
    nok = nok_three(a,b,c)
    print(f'Наименьшее общее кратное:{nok}')
else:
    print('Числа должны быть натуральными')