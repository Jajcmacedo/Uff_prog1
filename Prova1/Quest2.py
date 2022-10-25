while True:
    mes = int(input('Informe o mês: '))
    if mes == 2:
        ano = int(input('Entre com o ano (4 dígitos): '))
        if ano % 4 == 0 or ano % 400 == 0:
            print('Esse mês tem 29 dias')
        else:
            print('Esse mês tem 28 dias')
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print('Esse mês tem 31 dias')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print('Esse mês tem 30 dias')
    elif mes < 0 or mes > 12:
        print('Mês Inválido')
    if mes == 0:
        break
