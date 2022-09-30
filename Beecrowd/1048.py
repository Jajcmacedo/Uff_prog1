salariov = float(input())
if 0.00 < salariov <= 400:
    salario = salariov + (salariov * 0.15)
    print(f'Novo salario: {salario:.2f}')
    diferenca = salario - salariov
    print(f'Reajuste ganho: {diferenca:.2f}')
    print(f'Em percentual: 15 %')
elif 400 < salariov <= 800:
    salario = salariov + (salariov * 0.12)
    print(f'Novo salario: {salario:.2f}')
    diferenca = salario - salariov
    print(f'Reajuste ganho: {diferenca:.2f}')
    print(f'Em percentual: 12 %')
elif 800 < salariov <= 1200:
    salario = salariov + (salariov * 0.10)
    print(f'Novo salario: {salario:.2f}')
    diferenca = salario - salariov
    print(f'Reajuste ganho: {diferenca:.2f}')
    print(f'Em percentual: 10 %')
elif 1200 < salariov <= 2000:
    salario = salariov + (salariov * 0.07)
    print(f'Novo salario: {salario:.2f}')
    diferenca = salario - salariov
    print(f'Reajuste ganho: {diferenca:.2f}')
    print(f'Em percentual: 7 %')
elif 2000 < salariov:
    salario = salariov + (salariov * 0.04)
    print(f'Novo salario: {salario:.2f}')
    diferenca = salario - salariov
    print(f'Reajuste ganho: {diferenca:.2f}')
    print(f'Em percentual: 4 %')
