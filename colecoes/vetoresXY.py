vetX, vetY, cx, cy, cont, cX, cY = [], [], 1, 1, 0, 0, 0
soma, produto, diferenca, intersect, union = [], [], [], 0, 0
print('===========================')
print('  CALCULANDO DOIS VETORES  ')
print('===========================')
print('OBS: Não pode valores\nrepeditos!')
print('Valores de A:')
while len(vetX) <= 4:
    x = int(input(f'Diga o {cx}º valor X: '))
    vetX.append(x)
    print('--------------------------------')
    if cx == 5:
        # O algoritmo em ambos os loops (vetX e vetY) irá percorrer toda lista procurando valores semelhantes
        # se uma quantidade de valores repetidos sejam iguais ou acima de 2, removerá os valores repetidos
        # cont irá contar a quantidade de valores repetidos no algoritmo.
        for ch, va in enumerate(vetX):
            cont = 0
            for i, v in enumerate(vetX):
                if va == v:  # Compara os valores, começando com valor fixo do vetor e comparando com os outros valores percorrendo todo vetor para encontrar valores iguais e removê-los.
                    cont = cont + 1
                if cont >= 2 and va == v:
                    vetX.pop(i)
                    cX = cX + 1  # conta a quantidade de vezes que um valor foi repetido no vetor a diferença dele para o cont, é que ele guarda a quantidade e não por intervalo de comparação
        if cX > 0:
            print(f'Há {cX} valore(s) repetido(s) no vetor X!')
            print('Tente novamente...')
            cx = cx - cX
            cX = 0
    cx = cx + 1
print('Valores de B:')
while len(vetY) <= 4:
    y = int(input(f'Diga o {cy}º valor Y: '))
    vetY.append(y)
    print('--------------------------------')
    if cy == 5:
        for ch, va in enumerate(vetY):
            cont = 0
            for i, v in enumerate(vetY):
                if va == v:
                    cont = cont + 1
                if cont >= 2 and va == v:
                    vetY.pop(i)
                    cY = cY + 1
        if cY > 0:
            print(f'Há {cY} valore(s) repetido(s) no vetor Y!')
            print('Tente novamente...')
            cy = cy - cY
            cY = 0
    cy = cy + 1
for c in range(4):
    soma.append(vetX[c] + vetY[c])
    produto.append(vetX[c] * vetY[c])
    diferenca.append(vetX[c] % vetY[c])
    intersect = set(vetX).intersection(set(vetY))
    union = set(vetX).union(vetY)
print('==========================================================')
print('Calculo de vetores: ')
print(f'Vetor X: {vetX}')
print(f'Vetor Y: {vetY}')
print(f'Soma dos vetores: {soma}')
print(f'Produto dos vetores: {produto}')
print(f'Diferença dos vetores: {diferenca}')
print(f'Intersect dos vetores: {intersect}')
print(f'União dos vetores: {union}')
