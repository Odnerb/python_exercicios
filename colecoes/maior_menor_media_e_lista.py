valores = []
for c in range(1, 6):
    v = int(input(f'Diga o {c}º valor: '))
    valores.append(v)
print('-----------------------------------')
print(f'Valores: {valores}')
print(f'Maior valor: {max(valores)}')
print(f'Menor valor: {min(valores)}')
print(f'Média dos valores: {sum(valores)/len(valores)}')

