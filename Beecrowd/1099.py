N = int(input())

for i in range(N):
    linha = [int (num) for num in input().split(" ")]
    X = min(linha) #o menor sempre em X
    Y = max(linha)
    soma = 0
    for num in range(X+1,Y):
            if num%2==1:
                soma+=num
    print(soma)

##Solucionado por: https://github.com/mcavalca/uri-python

#n = int(input())
#for i in range(n):
#    x, y = input().split()
#    lista = [x, y]
#    lista.sort()
#    a = lista[0]
#    b = lista[1]
#    soma = 0
#    int(a)
#    int(b)
#    j = 0
#    for j in range((a + 1), b):
#        int(j)
#        if j % 2 != 0:
#            soma += j
#    print(soma)
