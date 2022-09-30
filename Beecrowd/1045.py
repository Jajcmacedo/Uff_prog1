while True:
    a, b, c = list(map(float, input().split()))
    if a > 0 and b > 0 and c > 0:
        break
lista = [a, b, c]
lista.sort()
a1 = lista[2]
b1 = lista[1]
c1 = lista[0]
if a1 >= b1 + c1:
    print('NAO FORMA TRIANGULO')
elif (a1 ** 2) == ((b1 ** 2) + (c1 ** 2)):
    print('TRIANGULO RETANGULO')
elif (a1 ** 2) > ((b1 ** 2) + (c1 ** 2)):
    print('TRIANGULO OBTUSANGULO')
elif (a1 ** 2) < ((b1 ** 2) + (c1 ** 2)):
    print('TRIANGULO ACUTANGULO')
if a1 == b1 and b1 == c1:
    print('TRIANGULO EQUILATERO')
elif a1 == b1 or b1 == c1 or c1 == a1:
    print('TRIANGULO ISOSCELES')
