# Algoritmo que cálcula elementos abaixo da diagonal principal de
# uma matriz 3x3
from typing import List

matriz: List[List[int]] = [[1, 2, 3], [4, 15, 6], [7, 8, 9]]

for _ in matriz:
    print(end='[')

    for c in _:
        print(f'{c:2}', end=' ')

    print(']')

if __name__ == '__main__':
    soma = matriz[1][0] + matriz[2][0] + matriz[2][1]
    print('================================================')
    print(f'A soma da diagonal principal é: {matriz[1][0]} + {matriz[2][0]} + {matriz[2][1]} = {soma}')


