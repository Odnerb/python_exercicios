v = int(input('Informe um número: '))
if v > 0:
    for i in range(1, v+1):
        if v % i == 0:
            print(f'{i} é divisor de {v}')
