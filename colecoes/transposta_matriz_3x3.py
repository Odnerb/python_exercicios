# Algoritmo que cálcula e imprime sua transposta

print('Matriz A')
matriz = [[1, 2, 3], [4, 15, 6]]
for _ in matriz:
    print(end='[')
    for c in _:
        print(f'{c:2}', end=' ')
    print(']')
transposta = [[matriz[0][0], matriz[1][0]], [matriz[0][1], matriz[1][1]], [matriz[0][2], matriz[1][2]]]
print('============================')
print("Matriz transposta: A'")
for _ in transposta:
    print(end='[')
    for c in _:
        print(f'{c:2}', end=' ')
    print(']')

