# imprimir a soma de todos os elementos das colunas ímpares
# imprimir média aritmética dos elementos da segunda e quartas colunas
# substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2
# imprimir raiz modificada

matriz = [[0, 1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10, 11],
          [12, 13, 14, 15, 16, 17]]
impar, ma_segColuna, ma_terColuna = 0, 0, 0
print('Matriz antes: ')
for linha in matriz:
    print(end='[ ')
    for c, num_coluna in enumerate(linha):
        print(f'{num_coluna:2}', end=' ')
        if num_coluna % 2 == 1:
            impar += num_coluna
        if c == 1:
            ma_segColuna += num_coluna
        if c == 3:
            ma_terColuna += num_coluna
    print(']')
print()
print(f'A soma dos valores impares por coluna: {impar}')
print(f'A média aritmética da segunda coluna: {ma_segColuna}')
print(f'A média aritmética da terceira coluna: {ma_terColuna}\n')
# Exercício pede para somar os resultados da segunda e quarta
# coluna e substituir pelos números da sexta coluna.
matriz[0][5] = ma_segColuna + ma_terColuna
matriz[1][5] = ma_segColuna + ma_terColuna
matriz[2][5] = ma_segColuna + ma_terColuna
print('Matriz depois: ')
for linha in matriz:
    print(end='[ ')
    for num_coluna in linha:
        print(f'{num_coluna:2}', end=' ')
    print(']')


