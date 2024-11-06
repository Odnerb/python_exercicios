# Matriz 4x4 que conta o total de valores maior que 10

matriz = []
integra = 0
qtMaiores = 0
for c in range(16):
    v = int(input(f'Diga o {c+1}º valor: '))
    matriz.append(v)
    if len(matriz) == 16:
        for cont in range(4):
            print()
            for i in range(4):
                if i == 0:
                    print(end='[  ')
                print(matriz[integra], end='  ')
                if i == 3:
                    print(end=']')
                integra = integra + 1
        print()
for valor in matriz:
    if valor > 10:
        print(valor)
        qtMaiores = qtMaiores + 1
print('---------------------------------------------------------------------')
print(f'Vetores da matriz = {matriz}')
print(f'O total de valores maior que 10 são {qtMaiores}')
