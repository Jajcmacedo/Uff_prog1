soma = 0
x = 0
while x != 1:
    linha = [int(num) for num in input().split(" ")]
    m = min(linha)
    n = max(linha)
    soma = 0
    if m <= 0 or n <= 0:
        x = 1
    if x != 1:
        for i in range (m, (n + 1)):
            soma += i
            print(i, end=" ")
            if i == n:
                print(f'Sum={soma}')
