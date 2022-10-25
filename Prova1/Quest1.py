n = int(input('Entre com um valor inteiro de 0 a 10: '))
t1 = 1
t2 = 1
t = 0
if 0 < n <= 2:
    print(f'F({n}) = {t1}')
elif n == 0:
    print('F(0) não existe.')
else:
    for x in range(n-2):
        t = t1 + t2
        t1 = t2
        t2 = t
    print(f'F({n}) = {t}')

