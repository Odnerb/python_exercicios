vet, vetPI = [], []
for c in range(0, 10):
    a = int(input(f'Diga o {c+1}º vetor: '))
    vet.append(a)
for c in range(0, 10):
    if c == 0 or c % 2 == 0:
        vetPI.append(vet[c] + vet.index(c+1))
    else:
        vetPI.append(vet[c] * vet.index(c+1))
print(f'Vetor: {vet}')
print(f'Vetor Par Impar: {vetPI}')
