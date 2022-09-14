n = int(input('Informe um número de 5 dígitos para descobrirmos se é um palíndromo:'))
if len(str(n)) == 5:
    if str(n) == str(n)[::-1]:
        print('É um palíndromo')
    else:
        print('Não é um palíndromo')
else:
    print('O número precisa conter 5 dígitos!')