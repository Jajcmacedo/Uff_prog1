while True:
    a, b, c = [int(x) for x in input().split()]
    if -100 <= a <= 100 and -100 <= b <= 100 and -100 <= c <= 100:
        break
if a > b:
    if c > b:
        print(':)')
    else:
        if (b - c) < (a - b):
            print(':)')
        else:
            print(':(')
elif a < b:
    if c < b:
        print(':(')
    else:
        if (b - c) > (a - b):
            print(':(')
        else:
            print(':)')
else:
    if c > a:
        print(':)')
    else:
        print(':(')
