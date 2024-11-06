# Algoritmo que cálcula elementos acima da diagonal principal de
# uma matriz 3x3

matriz = [[1, 2, 3], [4, 15, 6], [7, 8, 9]]
for _ in matriz:
    print(end='[')
    for c in _:
        print(f'{c:2}', end=' ')
    print(']')
soma = matriz[0][1] + matriz[0][2] + matriz[1][2]
print('================================================')
print(f'A soma da diagonal principal é: {matriz[0][1]} + {matriz[0][2]} + {matriz[1][2]} = {soma}')


