print('-------VETORES-------')
vet = []
for c in range(1, 11):
    n = int(input(f'{c}º valor: '))
    vet.append(n)
print('--------------------------------------------')
print(f'Vetores da lista: {vet}')
print(f'Maior número: {max(vet)}, posição: {vet.index(max(vet))}')

