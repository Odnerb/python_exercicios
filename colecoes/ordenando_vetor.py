# Ordenando valores de entrada inseridos pelo o usuário!
# somente valores inteiros.
print('----------------------------')
print('     Digite dez valores     ')
print('       fora de ordem!       ')
print('----------------------------')
vetor = []
for c in range(10):
    v = int(input(f'{c+1}º valor: '))
    vetor.append(v)
    vetor.sort()
print(f'Vetor ordenado: {vetor}')