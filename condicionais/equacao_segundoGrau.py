import math
print('===========================')
print('=     EQUAÇÃO 2ª GRAU     =')
print('=   Encontrando raízes    =')
print('===========================')
a = int(input('ax²: '))
b = int(input('b: '))
c = int(input('c: '))
delta = (b**2) - (4*a*c)
print('===========================')
print(f'Delta: {delta}')
if a > 0 and delta >= 0:
    raizP = delta
    raizN = delta
    raizP = math.pow(raizP, 1 / 2)
    raizN = math.pow(raizN, 1 / 2)
    xP = ((-b) + raizP) / 2 * a
    xN = ((-b) - raizN) / 2 * a
    if delta == 0:
        if xP > 0:
            print(f'XI = {xP:.1f} Raiz única.')
        elif xN < 0:
            print(f'XII = {xN:.1f} Raiz única.')
    elif delta >= 0:
        print(f'XI = {xP:.1f}\nXII = {xN:.1f}')
else:
    print('Não possui raiz')
print('===========================')
