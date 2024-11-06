# Matriz 4 x 4 com produto do valor da linha e da coluna de cada elemento

produto, posicao, cont = [], [], 1
for c in range(4):
    for i in range(4):
        a = int(input(f'{cont}º valor A: '))
        b = int(input(f'{cont}º valor B: '))
        print('--------------------------------------')
        produto.append(a * b)
        cont += 1
cont = 0
for c in range(4):
    print()
    print('[ ', end='')
    for i in range(4):
        print(f'{produto[cont]}', end=' ')
        cont += 1
    print(f']', end='')
cont = 0
for l in range(1, 5):
    if len(posicao) == 2:
        break
    for c in range(1, 5):
        if produto.index(produto[cont]) == produto.index(max(produto)):
            posicao.extend([l, c])
        cont += 1
print()
print('---------------------------------------------')
print(f'Maior valor da lista: {max(produto)}, Posição - {posicao}')

