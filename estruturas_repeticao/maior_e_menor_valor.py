print('------------------------------')
print('   MAIOR E MENOR VALOR LIDO   ')
print('------------------------------')
i = 1
maior = 0
menor = 0
while i < 10:
    v = float(input(f'Diga o {i}º valor: '))
    if v > maior:
        maior = v
    elif v < menor:
        menor = v
    i = i + 1
print('-----------------------------')
print(f'Maior valor digitado: {maior}')
print(f'Menor valor digitado: {menor}')
print('-----------------------------')
