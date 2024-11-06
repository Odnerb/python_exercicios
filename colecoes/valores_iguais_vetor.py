from collections import Counter
vetor, s, valIguais = [], 0, []
for c in range(1, 11):
    n = int(input(f'Diga o {c}º valor:'))
    vetor.append(n)
totValores = Counter(vetor)
for c, v in enumerate(totValores):
    if totValores[v] > 1:
        valIguais.append(v)
print('=====================================')
print(f'Lista: {vetor}')
print(f'Valores iguais na lista: {valIguais}')
