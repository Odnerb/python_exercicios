print('-------------------------')
print('-   VETORES A, B e C    -')
print('-------------------------')
vetA, vetB, vetC, c = [], [], [], 0
for c in range(1, 3):
    for i in range(0, 10):
        if c == 1:
            a = int(input(f'Diga o {i+1}º valor de A: '))
            vetA.append(a)
        elif c == 2:
            b = int(input(f'Diga o {i+1}º valor de B: '))
            vetB.append(b)
for i in range(0, 10):
    c = vetA[i] - vetB[i]
    vetC.append(c)
print('===============================================')
print(f'Vetor A: {vetA}')
print(f'Vetor B: {vetB}')
print(f'Vetor C: {vetC}')
print('===============================================')
