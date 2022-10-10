import random
vetor = []
print(f'O dado será lançado 50 vezes.')
for x in range(50):
    vetor.append(random.randint(1, 6))
porce = (vetor.count(6) * 100) / 50
print(f'O percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos é de {porce}%')
