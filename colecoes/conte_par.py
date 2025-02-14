from typing import List

print('  CONTE PAR DOS VETORES  ')
print('=========================')

vetores: List[int] = []
par: int = 0

for i in range(1, 11):
    vetor = int(input(f'Diga o {i}º: '))
    vetores.append(vetor)
print('-_-_-_-_-_-_-_-_-_-_-_-_-_')

if __name__ == '__main__':
    for c, v in enumerate(vetores):
        if v % 2 == 0:
            par: int = par + 1
    print('===========================')
    print(f'A lista possui {par}')
