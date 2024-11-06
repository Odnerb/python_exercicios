print('  CONTE PAR DOS VETORES  ')
print('=========================')
vetores, par = [], 0
for i in range(1, 11):
    vetor = int(input(f'Diga o {i}º: '))
    vetores.append(vetor)
print('-_-_-_-_-_-_-_-_-_-_-_-_-_')
for c, v in enumerate(vetores):
    if v % 2 == 0:
        par = par + 1
print('===========================')
print(f'A lista possui {par}')
