l = int(input('Digite até onde a sequencia de Fibonacci deva ir:'))
t1 = 1
if t1 < l:
    print(t1)
t2 = 1
if t2 < l:
    print(t2)
while (t1 + t2) <= l:
    t = t1 + t2
    print(t)
    t1 = t2
    t2 = t
