def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def nok(a, b):
    return (a * b) // nod(a, b)


A = int(input('Введите значение A: '))
B = int(input('Введите значение B: '))

if A <= 0 or B <= 0:
    print('Одно из чисел не является натуральным')
else:
    NOD = nod(A, B)
    NOK = nok(A, B)
    print(f'Наибольший общий делитель (НОД) чисел {A} и {B}: {NOD}')
    print(f'Наименьшее общее кратное (НОК) чисел {A} и {B}: {NOK}')