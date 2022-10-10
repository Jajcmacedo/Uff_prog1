status = 'false'
lista = [int(input(f'{i+1}º número: ')) for i in range(5)]
x = 0
n = int(input('Qual número vc deseja procurar? '))
while x < 5:
    if n == lista[x]:
        print('O valor {0} se encontra na {1}ª posição:'.format(n, x + 1))
        status = 'true'
    x += 1
if status == 'false':
    print('-1')
