vet = [int(input(f'{i+1}º número de 20: ')) for i in range(20)]
pos = []
sendup = []
for j in vet:
    if j > 0:
        pos.append(j)
        if sendup.count(j) < 1:
            sendup.append(j)
print('Vetor "vet":', vet)
print('Vetor "pos":', pos)
print('Vetor "sendup":', sendup)
