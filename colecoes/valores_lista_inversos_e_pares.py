print('======================')
print('= = Lista de Pares = =')
print('======================')
lista = []
for c in range(1, 7):
    n = int(input(f'Diga o {c}º valor: '))
    if n % 2 == 0:
        lista.append(n)
print(f'Lista: {lista[::-1]}')
