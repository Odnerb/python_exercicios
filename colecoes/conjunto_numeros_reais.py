print(' CONJUNTOS DOS NÚMEROS REAIS ')
print('=============================')

from typing import List

c: int = 10
conjQ: List[float] = []
quadQ: List[float] = []

for i in range(1, c+1):
    q = float(input('Diga um número real: '))
    conjQ.append(q)
    quadQ.append(float(f'{q**2:.2f}'))

if __name__ == '__main__':
    print(f'Elementos primeiro vetor: {conjQ}')
    print(f'Elementos segundo vetor: {quadQ}')
