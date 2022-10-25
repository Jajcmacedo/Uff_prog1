lista = []
listaor = []
listapar = []
listaimp = []
listaimpi = []
n = int(input())
for x in range(n):
    valor = int(input())
    lista.append(valor)
while lista != []:
    listaor.append(min(lista))
    lista.remove(min(lista))
for p in range(len(listaor)):
    if listaor[p] % 2 == 0 or listaor[p] == 0:
        listapar.append(listaor[p])
    else:
        listaimp.append(listaor[p])
listaimpi = listaimp[::-1]
for x in range(len(listapar)):
    print(listapar[x])
for x in range(len(listaimpi)):
    print(listaimpi[x])
