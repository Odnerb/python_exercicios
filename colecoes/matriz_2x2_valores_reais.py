# Duas Matrizes 2 x 2 com valores reais com opções de:
# soma;
# subtração;
# constante;
# imprimir matrizes;
# Será mostrado na tela as opções e retornado o resultado

def menu():
    print('===========================')
    print('=     M A T R I Z E S     =')
    print('===========================')
    print('Selecione a opção:')
    print('a) - Somar matrizes')
    print('b) - Subtrair matrizes')
    print('c) - Adicionar uma constante às duas matrizes')
    print('d) - Imprimir matrizes')


continuar = 's'
constante, calculo = 0, 0
a, b = [[2.4, 3.7], [7.1, 6.3]], [[5.0, 1.1], [3.9, 8.6]]
matriz = []

while continuar == 's':
    menu()
    op = str(input('Diga a letra -> '))
    if op == 'a':
        matriz.extend([[a[0][0] + b[0][0], a[0][1] + b[0][1], 0],
                       [a[1][0] + b[1][0], a[1][1] + b[1][1], 0],
                       [0, 0, 0]])
        for _ in matriz:
            print(end='[ ')
            for c in _:
                print(end=f'{c:4n} ')
            print(']')
    elif op == 'b':
        matriz.extend([[a[0][0] - b[0][0], a[0][1] - b[0][1], 0],
                       [a[1][0] - b[1][0], a[1][1] - b[1][1], 0],
                       [0, 0, 0]])
        for _ in matriz:
            print(end='[ ')
            for c in _:
                print(end=f'{c:4n} ')
            print(']')
    elif op == 'c':
        constante = float(input('Diga a constante: '))
        print('Matriz A')
        for _ in a:
            print(end='[ ')
            for c in _:
                print(end=f'{c + constante:4n} ')
            print(']')
        print()
        print('Matriz B')
        for _ in b:
            print(end='[ ')
            for c in _:
                print(end=f'{c + constante:4n} ')
            print(']')
    elif op == 'd':
        print('Matriz A')
        for _ in a:
            print(end='[ ')
            for c in _:
                print(end=f'{c:4n} ')
            print(']')
        print('Matriz B')
        for _ in b:
            print(end='[ ')
            for c in _:
                print(end=f'{c:4n} ')
            print(']')
    print('Continuar? [s/n]')
    continuar = str(input())
    matriz = []
    if continuar == 'n':
        break




