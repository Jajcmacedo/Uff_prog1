n1, n2, n3, n4 = [float(x) for x in input().split()]
n1 = (2 * n1)
n2 = (3 * n2)
n3 = (4 * n3)
n4 = (1 * n4)
media = (n1 + n2 + n3 + n4) / 10
print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    mediaf = (exame + media) / 2
    if mediaf < 5:
        print('Aluno reprovado.')
    else:
        print('Aluno aprovado.')
    print(f'Media final: {mediaf:.1f}')
