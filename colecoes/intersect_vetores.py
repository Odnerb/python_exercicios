vetA, vetB = [], []
c = 1
while len(vetA) <= 10 and len(vetB) <= 10:
    if len(vetA) <= 10:
        vA = int(input(f'Diga o {c}º valor do vetor A: '))
        if len(vetA) < 10:
            vetA.append(vA)
    if len(vetB) <= 10:
        vB = int(input(f'Diga o {c}º valor do vetor B: '))
        if len(vetB) < 10:
            vetB.append(vB)
    if len(vetA) == 10 and len(vetB) == 10:
        break
    c = c + 1
vetIntersect = set(vetA).intersection(set(vetB))
print('=======================================================')
print(f'{set(vetA)}')
print(f'{set(vetB)}')
print(vetIntersect)
