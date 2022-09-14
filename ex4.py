m20 = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
d = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
c = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos',
     'novecentos']
m = ['', 'mil', 'dois mil', 'três mil', 'quatro mil', 'cinco mil', 'seis mil', 'sete mil', 'oito mil', 'nove mil']
while True:
    n = int(input('Digite um número inteiro entre 0 e 9999:'))
    if 0 <= n <=9999:
        break
if n == 1000:
    print('mil')
elif n == 100:
    print('cem')
elif n == 0:
    print('zero')
else:
    if 1000 < n <=9999:
        print(m[int(str(n)[0])], end='')
        n = n - int(str(n)[0])*1000
        if n !=0:
            print('', end=' ' )
    if 100 < n < 1000:
        print(c[int(str(n)[0])], end='')
        n = n - int(str(n)[0])*100
        if n !=0:
            print(' e', end=' ' )
    if n < 20:
        print(m20[n])
        n = 0
    elif n >= 20:
        print(d[int(str(n)[0])], end=' ')
        n = n - int(str(n)[0])*10
    if n != 0:
        print('e', m20[n])

#Código adaptado do membro GeBEfte da plataforma Brainly.