print('---------------------------------')
print('- VETORES POSITIVOS E NEGATIVOS -')
print('---------------------------------')
vetor, calc, s = [], [], []
for c in range(1, 11):
    v = float(input(f'Diga o {c}º valor: '))
    vetor.append(v)
for c, v in enumerate(vetor):
    if v < 0:
        calc.append(v)
    elif v >= 0:
        s.append(v)
print('===============================================')
print(f'Vetor: {vetor}')
print(f'Tot. Negativos: {len(calc)}, soma: {sum(calc)}')
print('-----------------------------------------------')
print(f'Tot. Positivos: {len(s)}, soma: {sum(s)}')
print('===============================================')
