import math
x1, y1 = [int(x) for x in (input('Informe as coordenas x e y (x,y) do primeiro ponto:').split(','))]
x2, y2 = [int(x) for x in (input('Informe as coordenas x e y (x,y) do segundo ponto:').split(','))]
x3, y3 = [int(x) for x in (input('Informe as coordenas x e y (x,y) do terceiro ponto:').split(','))]
A = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
B = math.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
C = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
if ((A + B > C) and (A + C > B) and (B + C > A)):
    if (A == B and B == C):
        print('Equilátero')
    elif (A == B or B == C or C == A):
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não é um triângulo')