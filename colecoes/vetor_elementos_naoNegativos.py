vetor = []
for c in range(1, 11):
    valor = float(input(f'{c}º valor: '))
    if valor <= 0:
        vetor.append(0)
    else:
        vetor.append(valor)
print(f'Vetor: {vetor}')

