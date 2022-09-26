n = int(input('Digite quantos némeros a  sequencia de Fibonacci deve ter:'))
t1 = 1
if t1 <= n:
    print(t1)
t2 = 1
if t2 < n:
    print(t2)
for n in range(n-2):
    t = t1 + t2
    print(t)
    t1 = t2
    t2 = t

#O enunciado está um pouco confuso, mas pelo que eu entendi é para o usuario colocar o número de elementos da sequencia de Fibonacci que ele deseja. Correto?