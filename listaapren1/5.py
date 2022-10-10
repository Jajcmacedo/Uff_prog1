contfla = 0
contvas = 0
contflu = 0
contbot = 0
contouts = 0
mediafla = 0
mediavas = 0
mediaflu = 0
mediabot = 0
mediaouts = 0
nitouts = 0
pentrevistadas = 0
continuar = True
while continuar == True:
    time = int(input('Qual o seu clube de futebol de preferência (1 – Flamengo, 2 – Vasco, 3 – Fluminense, 4 – Botafogo, 5 – Outros)? '))
    if time != 5:
        if time == 1:
            contfla += 1
            mediafla += float(input('Qual o seu salário? '))
        elif time == 2:
            contvas += 1
            mediavas = float(input('Qual o seu salário? '))
        elif time == 3:
            contflu += 1
            mediaflu += float(input('Qual o seu salário? '))
        elif time == 4:
            contbot += 1
            mediabot += float(input('Qual o seu salário? '))
        nniteroi = int(input('Qual a sua cidade natal (1 – Niterói, 2 – Outra)? '))
    elif time == 5:
        contouts += 1
        mediaouts += float(input('Qual o seu salário? '))
        nniteroi = int(input('Qual a sua cidade natal (1 – Niterói, 2 – Outra)? '))
        if nniteroi == 1:
            nitouts += 1

    while True:
        print("Novo cadastro? (1-sim 2-nao)")
        novo = int(input())
        if novo == 2:
            continuar = False
            break
        elif novo == 1:
            continuar = True
            break
    pentrevistadas += 1
if contfla > 0:
    mediaflaf = mediafla / contfla
else:
    mediaflaf = 0
if contvas > 0:
    mediavasf = mediavas / contvas
else:
    mediavasf = 0
if contflu > 0:
    mediafluf = mediaflu / contflu
else:
    mediafluf = 0
if contbot > 0:
    mediabotf = mediabot / contbot
else:
    mediabotf = 0
if contouts > 0:
    mediaoutsf = mediaouts / contouts
else:
    mediaoutsf = 0

print('Torcedores do Flamengo:', contfla)
print('Torcedores do Vasco:', contvas)
print('Torcedores do Fluminense:', contflu)
print('Torcedores do botafogo:', contbot)
print('Torcedores de Outros:', contouts)
print(f'Médias salarial dos torcedores do Flamengo: {mediaflaf:.2f}')
print(f'Médias salarial dos torcedores do Vasco: {mediavasf:.2f}')
print(f'Médias salarial dos torcedores do Fluminense: {mediafluf:.2f}')
print(f'Médias salarial dos torcedores do botafogo: {mediabotf:.2f}')
print(f'Médias salarial dos torcedores de Outros: {mediaoutsf:.2f}')
print(f'Número de pessoas nascidas em Niterói e que não torcem para nenhum dos principais clubes do Rio', nitouts)
print('Número de pessoas entrevistadas:', pentrevistadas)
