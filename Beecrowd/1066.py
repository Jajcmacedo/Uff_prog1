npar = 0
nimpar = 0
npositivo = 0
nnegativo = 0
for i in range(5):
    v = int(input())
    if v > 0:
        npositivo = npositivo + 1
    elif v < 0:
        nnegativo = nnegativo + 1
    if v % 2 == 0:
        npar = npar + 1
    elif v % 2 != 0:
        nimpar = nimpar + 1
print(npar, 'valor(es) par(es)')
print(nimpar, 'valor(es) impar(es)')
print(npositivo, 'valor(es) positivo(s)')
print(nnegativo, 'valor(es) negativo(s)')
