controle = 0
m = 0
p = 0
n = int(input())
for i in range(1, 100):
    v = int(input())
    if controle < v:
        m = v
        p = i + 1
        controle = v
print(m)
print(p)
