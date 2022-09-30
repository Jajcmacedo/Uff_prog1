nota_soma = 0
cont = 0
continuar = True

while continuar == True:
    nota = float(input())

    if nota >= 0.0 and nota <= 10:
        nota_soma += nota
        cont += 1

        if cont == 2:

            print("media = %.2f" % (nota_soma / 2))
            cont = 0
            nota_soma = 0

            while True:
                print("novo calculo (1-sim 2-nao)")
                novo = int(input())
                if novo == 2:
                    continuar = False
                    break
                elif novo == 1:
                    continuar = True
                    break

    else:
        print("nota invalida")

#http://muitomaiscodigoss.blogspot.com/2018/05/uri-problema-1118-varias-notas-com.html
#x = 1
#nsoma = 0
#cont = 0
#while x != 2:
#    c = 0
#    v = 0
#    n = float(input())
#    if 0 <= n <= 10:
#        nsoma += n
#        cont += 1
#       if cont == 2:
#            print(f'media = {(nsoma / 2):.2f}')
#            nsoma = 0
#            cont = 0
#            while True:
#                x = int(input('novo calculo (1-sim 2-nao)'))
#                if x == 1 or x == 2:
#                    break
#    else:
#        print('nota invalida')
