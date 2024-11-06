v = int(input('Informe o valor: '))
sP = 0
sN = 0
if (v > 0) and (v < 1000):
    for i in range(1, v):
        if (i % 3 == 0) or (i % 5 == 0):
            sP = sP + i
            print(i)
elif (v < 0) and (not v > 1000):
    for i in range(-1, v-1, -1):
        if (i % 3 == 0) or (i % 5 == 0):
            sN = sN - i
            print(i)
if v < 1000:
    print('------------------------------------')
    print('Soma dos valores múltiplos de 3 ou 5')
    if v > 0:
        print(f'Total: {sP}')
    else:
        print(f'Total: -{sN}')
    print('------------------------------------')
else:
    print('ERRO: Informe um valor menor que mil')
