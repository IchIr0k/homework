def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


A = int(input())
B = int(input())

nok = gcd(A, B)
nod = lcm(A, B)

print(nok)
print(nod)
