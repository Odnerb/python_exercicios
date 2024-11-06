print('   Somando impares   ')
print('---------------------')
i = int(input('Inicio: '))
f = int(input('Fim: '))
s = 0
print('---------------------')
for c in range(i, f, 1):
    if i > f:
        print('Intervalo de valores inválido.')
    else:
        if c % 2 == 1:
            s = s + c
print(f'Soma dos impares neste intervalo: {s}')
