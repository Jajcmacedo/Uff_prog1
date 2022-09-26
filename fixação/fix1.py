import random
n = int(input('Digite um número de 1 a 10:'))
cont = 0
x= 0
while x != n:
    cont = cont + 1
    r = random.randint(0, 10)
    s = random.randint(0, 10)
    x = r + s
    if x != n:
        print('Soma do números gerados:', x, '. Não foi dessa fez!')
    else:
        print('Depois de', cont,'vezes, a soma de dois números aleatórios é o valor que escolhemos:', n)

#A forma como está no enunciado poderia gerar um loop infinito, pois a soma de 2 números inteiros maiores que zero seria >= 2.