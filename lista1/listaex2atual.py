valor = int(input('Digite um valor em centavos:'))
while valor != 0:
    Rea1 = valor

rea1 = int(valor / 100)
valor = valor - (rea1 * 100)
cent50 = int(valor / 50)
valor = valor - (cent50 * 50)
cent25 = int(valor / 25)
valor = valor - (cent25 * 25)
cent10 = int(valor / 10)
valor = valor - (cent10 * 10)
cent5 = int(valor / 5)
valor = valor - (cent5 * 5)
cent1 = valor

print('Moedas de 1 real = ', rea1)
print('Moedas de 50 centavos = ', cent50)
print('Moedas de 25 centavos = ', cent25)
print('Moedas de 10 centavos = ', cent10)
print('Moedas de 5 centavos = ', cent5)
print('Moedas de 1 centavos = ', cent1)
