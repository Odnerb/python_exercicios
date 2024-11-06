vetA, vetB, c = [], [], 1
while len(vetA) <= 9 and len(vetB) <= 9:
    a = int(input(f'{c}º valor de A: '))
    vetA.append(a)
    b = int(input(f'{c}º valor de B: '))
    vetB.append(b)
    c = c + 1
vetUnion = set(vetA).union(set(vetB))
print('==================================================')
print(f'Valor de A: {vetA}')
print(f'Valor de B: {vetB}')
print(f'União dos vetores: {vetUnion}')
