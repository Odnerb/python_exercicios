print('---------------------------')
print('- LENDO VALORES LISTA INT -')
print('-      INVERSAMENTE       -')
print('---------------------------')
lista = []
for c in range(1, 7):
    v = int(input(f'{c}º valor: '))
    lista.append(v)
print('---------------------------')
print(f'Lista inversa: {lista[::-1]}')
