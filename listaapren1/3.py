n = int(input('Quantos são os valores que deseja opter a soma dos quadrados? '))
soma = 0
for i in range(n):
    x = int(input(f'{i+1}ºvalor: '))
    soma += x ** 2
print(soma)