cont = 10
print('Informe 10 números inteiros')
lista = [int(input(f'{i+1}º número: ')) for i in range(10)]
for x in lista:
    if lista.count(x) >= 2:
        cont -= 1
print(cont)
