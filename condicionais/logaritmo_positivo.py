import math
n = int(input('Diga um valor inteiro: '))
if n < 0:
    print('"Número inválido')
else:
    log = math.log(n, 2)
    print(f'O logaritmo de {n} é {log:,.11f}')
