from typing import List

a: List[int] = []
b: List[int] = []

for i in range(0, 51):
    a.append(i)

    if i != 0 and i % 2 == 1:
        b.append(i)

if __name__ == '__main__':
    print('===============================================')
    print(f'Vetor A: {a}')
    print(f'Vetor B: {b}')
    print('===============================================')
