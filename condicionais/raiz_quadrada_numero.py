import math
num = int(input('Diga um número: '))
if num > 0:
    num = math.pow(num, 1/2)
    print(f'{num}')
else:
    print('Número inválido!')
