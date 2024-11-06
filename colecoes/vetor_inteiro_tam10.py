vetDez, cont = [], 0
for c in range(10):
    n = int(input(f'{c+1}º valor: '))
    vetDez.append(n)
print('============================================')
print(f'Vetor: {vetDez}')
for c, v in enumerate(vetDez):
    cont = 0
    for i in range(10):
        if v % (i+1) == 0:
            cont = cont + 1
        if v == i and v % 1 == 0 and cont == 2 and not (v != i and v % (i+1) == 0):
            print(f'O valor {v} é primo e está na posição: {vetDez.index(v)}')
