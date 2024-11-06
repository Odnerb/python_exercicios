# Lendo uma matriz 5x5 com valores, usuário digita o valor
# e recebe a posição do número.
cont, p = 0, []
matriz = [[10, 11, 12, 13, 14],
          [21, 22, 24, 26, 28],
          [30, 33, 37, 38, 39],
          [90, 91, 92, 94, 99],
          [43, 44, 50, 51, 57]]
for m in matriz:
    print(m)
print('----------------')
print('Escolha um número da matriz 5x5: ')
v = int(input(''))
for l, m in enumerate(matriz):
    for i in range(5):
        if m[cont] == v:
            p = [l+1, m.index(m[cont])+1]
        cont = cont + 1
    cont = 0
print('====================')
print(f'Posição de: {v} = {p}')
