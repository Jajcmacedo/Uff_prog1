n = int(input('Informe um número inteiro:'))
x = 1
while True:
    cont = 0
    while x <= n:
        if n % x == 0:
            print(x, 'é divisor de', n)
            cont = cont + 1
        x = x + 1
    if cont == 1 :
        print(n, 'não é um número primo.')
    elif cont == 2:
        print(n,'é um número primo.')
    else:
        print(n, 'não é um número primo.')
    n = int(input('Informe um número inteiro:'))
    x = 1
