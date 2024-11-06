print('Menor divisor de 1 a 20')
print('-----------------------------------')
n = int(input('Diga um número inteiro positivo: '))
print('-----------------------------------')
print(f'Os divisor de {n}, são:')
for c in range(1, 20):
    if c < 20:
        if n % c == 0:
            print(c, end=', ')
        else:
            break
