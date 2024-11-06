import math
num = int(input('Diga um número: '))
if num > 0:
    quad = num ** 2
    raizQ = math.pow(num, 1/2)
print('==================================================')
print(f'O número {num}² é igual a {quad}')
print(f'A raiz quadrada do número {num} é igual a {raizQ}')
print('==================================================')
