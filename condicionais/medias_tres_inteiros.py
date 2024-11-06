import math
print('    M É D I A S    ')
print('-------------------')
x = int(input('Valor de X: '))
y = int(input('Valor de Y: '))
z = int(input('Valor de Z: '))
n = 3
print('-------------------')
if x and y and z > 0:
    g = math.pow(x*y*z, 1/3)
    p = (x + (2*y) + (3*z))/6
    h = n/((1/x)+(1/y)+(1/z))
    # lembre-se, na média harmônica (n) é a quantidade de números (elementos) calculados!
    a = (x+y+z)/3
    tg = f'{g:.2f}'
    tp = f'{p:.2f}'
    th = f'{h:.2f}'
    ta = f'{a:.2f}'
    tg = tg.replace('.', ',')
    tp = tp.replace('.', ',')
    th = th.replace('.', ',')
    ta = ta.replace('.', ',')
    print(f'Valores: X = {x}; Y = {y}; Z = {z}')
    print(f'Média Geométrica: {tg}')
    print(f'Média Ponderada: {tp}')
    print(f'Média Harmônica: {th}')
    print(f'Média Aritmética: {ta}')
else:
    print('Insira valores inteiros positivos (acima de 0).\nTente novamente!')
