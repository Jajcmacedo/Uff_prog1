x = int(input('Informe um valor para X:'))
while x != 0:
    if x % 2 == 0:
        print(x + (x + 2) + (x + 4) + (x + 6) + (x + 8))
        break
    else:
        print((x + 1) + (x + 3) + (x + 5) + (x + 7) + (x + 9))
        break
