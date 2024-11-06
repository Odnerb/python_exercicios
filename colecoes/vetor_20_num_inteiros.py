# Eliminando elementos repetidos de um vetor
vetor = []
for c in range(1, 21):
    n = int(input(f'{c}º valor: '))
    vetor.append(n)
print('-------------------------------------')
print(f'lista: {set(vetor)}')
