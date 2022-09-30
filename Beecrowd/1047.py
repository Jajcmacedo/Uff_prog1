horai, minutoi, horaf, minutof = [int(x) for x in input().split()]
if horai < horaf:
    hora = horaf - horai
    if minutoi < minutof:
        minuto = minutof - minutoi
    if minutoi > minutof:
        hora = hora - 1
        minuto = (60 - minutoi) + minutof
    if minutoi == minutof:
        minuto = 0
if horai > horaf:
    hora = (24 - horai) + horaf
    if minutoi < minutof:
        minuto = minutof - minutoi
    if minutoi > minutof:
        hora = hora - 1
        minuto = (60 - minutoi) + minutof
    if minutoi == minutof:
        minuto = 0
if horai == horaf:
    if minutoi < minutof:
        minuto = minutof - minutoi
        hora = 0
    if minutoi > minutof:
        minuto = (60 - minutoi) + minutof
        hora = 23
    if minutoi == minutof:
        hora = 24
        minuto = 0
print('O JOGO DUROU', hora, 'HORA(S) E',minuto,'MINUTO(S)')
