import random
vetor = list()
soma = 0
nnove = 0
maior = 0
print(f'O dado será lançado 50 vezes.')
for x in range(50):
    var = random.randint(0, 20)
    vetor.append(var)
    soma += var
    nnove = vetor.count(9)
    maior = max(vetor)
print()
print(vetor)
print()
print('A soma dos valores armazenados no vetor é:', soma)
print()
print('O número de ocorrências do valor 9 é:', nnove)
print()
print('O maior valor armazenado no vetor é', maior)
print()
for j in range(len(vetor)):
    if maior == vetor[j]:
        print('O maior valor que é {0} se encontra na {1}ª posição:'.format(maior, j + 1))
