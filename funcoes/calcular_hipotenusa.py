# Achar a hipotenusa de um triângulo com catetos a e b
import math


def triangulo(a, b):
    h = math.sqrt((a**2) + (b**2))
    # Função round arredonda
    h = round(h, 2)
    return h


print('  HIPOTENUSA DO TRIÂNGULO  ')
print('=============================')
print('Informe os catetos de abaixo.')
x = float(input('Valor de A: '))
y = float(input('Valor de B: '))
print('_____________________________')

print(triangulo(x, y))
