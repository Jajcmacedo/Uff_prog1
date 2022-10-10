while True:
    n = int(input('Informe um número para saber se ele é triangular:'))
    x = 1
    soma = 0
    while soma < n:
        soma += x
        x += 1
    if soma == n:
        print(n, 'é um número perfeito.')
    else:
        print(n, 'não é um número perfeito.')
# Dúvida se é isso o que a professora quer