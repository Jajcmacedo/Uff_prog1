L = int(input('Digite até onde a sequencia de Fibonacci deva ir:'))
t1 = 1
if t1 < L:
    print(t1)
t2 = 1
if t2 < L:
    print(t2)
while (t1 + t2) <= L:
    t = t1 + t2
    print(t)
    t1 = t2
    t2 = t
