massa = float(input('Informe sua massa em Kg:'))
altura = float(input('Informe altura em metros:'))
imc = massa / (altura * altura)
if (imc < 18.5):
    print('Abaixo do peso')
elif ( 18.5 <= imc <= 24.9):
    print('Saudável')
elif (25.0 <= imc <= 29.9):
    print('Obesidade Grau I')
elif (30.0 <= imc <= 34.9):
    print('Obesidade Grau II (severa)')
elif (imc >= 40.0):
    print('Obesidade Grau III (mórbida)')