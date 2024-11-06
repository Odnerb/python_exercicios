# Algoritmo que recebe valores reais aleatórios e depois os ordena.

vetor = []
for c in range(10):
    v = float(input(f'Diga o {c+1}º valor: '))
    vetor.append(v)
vetor.sort()
print('-------------------------------------------------')
print(f'Vetor ordenado: {vetor}')
