# Matriz 4x4 inferior com valores no intervalo de 1 a 20 e preenchidos por 0
# na parte superior.

matriz, cont = [], 0
for l in range(4):
    linha = []
    for c in range(4):
        m = int(input(f'{l+1}º linha, {c+1}º colunha valor: '))
        linha.append(m)
    matriz.append(linha)
for _ in range(4):
    for c in range(4):
        if matriz[0][1] == matriz[_][c] or matriz[0][2] == matriz[_][c] or matriz[0][3] == matriz[_][c]:
            matriz[_][c] = 0
        elif matriz[1][2] == matriz[_][c] or matriz[1][3] == matriz[_][c]:
            matriz[_][c] = 0
        elif matriz[2][3] == matriz[_][c]:
            matriz[_][c] = 0
print('---------------------------')
for _ in matriz:
    print(end='[ ')
    for c in _:
        print(f'{c:2}', end=' ')
    print(']')

