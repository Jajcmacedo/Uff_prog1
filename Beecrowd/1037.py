n = float(input())
if 0 <= n <= 25:
    print('Intervalo [0,25]')
elif 25 < n <= 50:
    print('Intervalo (25,50]')
elif 50 < n <= 75:
    print('Intervalo (50,75]')
elif 75 < n <= 100:
    print('Intervalo (75,100]')
elif n > 100 or n < 0:
    print('Fora de intervalo')
