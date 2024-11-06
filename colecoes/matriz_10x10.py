# Gerando Matriz 10x10 a partir de cálculo de fórmulas

matriz, cont = [], 0
for i in range(1, 11):
    linha = []
    for j in range(1, 11):
        if i < j:
            a = (2*i) + (7*j) - 2
            linha.append(a)
        elif i == j:
            a = ((3*i)**2) - 1
            linha.append(a)
        else:
            a = ((4*i)**3) - ((5*j)**2)
            linha.append(a)
    matriz.append(linha)
for linha in matriz:
    print('[', end=' ')
    for numero in linha:
        print(f'{numero:7}', end=' ')
    print(']')
