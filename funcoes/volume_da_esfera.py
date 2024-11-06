# Cálculando volume de uma esfera
import math

raio = float(input('Raio esfera (cm): '))


def volume_esfera(r):
    v = 4/3 * math.pi * r**3
    return f'{v:.2f}'


print(f'Volume da esfera: {volume_esfera(raio)} cm')
