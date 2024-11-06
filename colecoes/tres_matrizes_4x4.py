# Lendo duas matrizes e colocando os maiores valores de cada matriz
# em uma nova.

matriz_a = [[1, 5, 19, 14], [12, 25, 47, 10], [39, 44, 11, 38.77], [23, 32, 17, 61]]
matriz_b = [[48, 62, 19, 45], [22, 72, 18, 15.5], [34, 29, 91, 12], [1.56, 80, 73, 56]]
matriz_v, cont = [], 1
while cont <= 2:
    for _ in range(4):
        matriz_v.append(max(matriz_a[_]))
        matriz_v.append(max(matriz_b[_]))
        a = max(matriz_a[_])
        matriz_a[_].remove(a)
        b = max(matriz_b[_])
        matriz_b[_].remove(b)
    cont += 1
cont = 0
print('-----------------------------------')
print('Matriz com os maiores valores de'
      'cada posição:')
for l in range(4):
    print()
    print(end='[ ')
    for c in range(4):
        print(f'{matriz_v[cont]}', end=' ')
        cont += 1
    print(end=']')
