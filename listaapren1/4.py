x, y, = [int(xy) for xy in input().split('/')]
quociente = 0
cont = 0
soma = 0
while soma <= x:
    soma += y
    quociente += 1
soma -= y
quociente -= 1
resto = x - soma
print('Quociente:', quociente, 'Resto:', resto)
