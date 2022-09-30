a, b, c = [float(abc) for abc in (input().split(' '))]
TRIANGULO = (a * c) / 2
CIRCULO = 3.14159 * c ** 2
TRAPEZIO = ((a + b) * c) / 2
QUADRADO = b ** 2
RETANGULO = a * b
print(f'TRIANGULO: {TRIANGULO:.3f}')
print(f'CIRCULO: {CIRCULO:.3f}')
print(f'TRAPEZIO: {TRAPEZIO:.3f}')
print(f'QUADRADO: {QUADRADO:.3f}')
print(f'RETANGULO: {RETANGULO:.3f}')
