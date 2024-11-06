# Encontrando a posição do menor e maior valor
valores = []
for c in range(1, 6):
    v = int(input(f'{c}º valor: '))
    valores.append(v)
print(f'Valores lista: {valores}')
print('-------------------------------')
maior = valores.index(max(valores))
menor = valores.index(min(valores))
print(f'Posição maior valor: {maior+1}')
print(f'Posição menor valor: {menor+1}')
