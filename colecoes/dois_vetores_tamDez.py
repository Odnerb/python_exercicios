from typing import List

v1: List[int] = []
v2: List[int] = []

for c in range(0, 100):
    v = int(input(f'{c}º número: '))

    if v % 2 == 1 and len(v1) < 10:
        v1.append(v)

    elif v % 2 == 0 and len(v2) < 10:
        v2.append(v)

    elif len(v1) == 10 or len(v2) == 10:
        break

if __name__ == '__main__':
    print('==================================')
    print(f'Vetor impar: {v1}')
    print(f'Vetor par: {v2}')
