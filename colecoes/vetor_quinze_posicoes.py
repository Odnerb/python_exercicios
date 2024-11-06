# Algoritmo que apaga todos valores 0 do vetor e move qualquer número
# depois de 0 para o final do vetor.

vetor, vetP, c = [], 1, 1
while len(vetor) <= 14:
    v = int(input(f'Diga o {c}º valor: '))
    if v == 0:
        vetP = v
    elif vetP == 0 and v > 0:
        vetor.insert(0, v)
        vetP = v
    else:
        vetor.append(v)
    c = c + 1
print(vetor)
