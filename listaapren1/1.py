while True:
    n = int(input('Informe um número para saber se ele é perfeito:'))
    x = 1
    soma = 0
    while soma < n:
        if n % x == 0:
            soma += x
        x += 1
    if soma == n and soma != 1 and soma != 0:
        print(n,'é um número perfeito.')
    elif 1 == n or 0 == n:
        print(n, 'não é um número perfeito.')
    else:
        print(n, 'não é um número perfeito.')
