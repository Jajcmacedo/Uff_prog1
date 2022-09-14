import math
x1, y1 = [int(x) for x in (input('Informe as coordenas x e y (x,y) do primeiro ponto:').split(','))]
x2, y2 = [int(x) for x in (input('Informe as coordenas x e y (x,y) do segundo ponto:').split(','))]
distancia = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
print('A distância entre os pontos é de',distancia)