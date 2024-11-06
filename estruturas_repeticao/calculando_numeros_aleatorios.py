import math
print(' QUADRADO, CUBO E RAIZ QUADRADA ')
print('--------------------------------')
print('medida em cm')
print('--------------------------------')
n = 1
while n >= 1:
    print('Selecione a opção:\n[0] - Para sair\n[1] - Área do Quadrado\n[2] - Área do Cubo\n[3] - Raiz quadrada')
    op = int(input())
    if (op >= 1) and (op <= 3):
        vezes = int(input('Quantas vezes irá calcular? '))
        for c in range(1, vezes+1):
            if op == 1:
                n = float(input('Valor o 1º número: '))
                n2 = float(input('Valor o 2º número: '))
                aq = n*n2
                print('-----------------------------')
                print(f'O quadrado da área é {aq}cm² ')
                print('-----------------------------')
            elif op == 2:
                n = float(input('Valor o 1º número: '))
                n2 = float(input('Valor o 2º número: '))
                n3 = float(input('Valor o 3º número: '))
                c = n*n2*n3
                print('-------------------------')
                print(f'O cubo da área é {c}cm³ ')
                print('-------------------------')
            elif op == 3:
                n = float(input(f'Valor o {c}º número: '))
                rq = math.pow(n, (1/2))
                print('------------------------------')
                print(f'A raiz quadrada de {n:.0f} é {rq}')
                print('------------------------------')
            elif op <= 0:
                break
            else:
                print('ERRO: Tente novamente!')
        cont = int(input('Quer continuar?\n[1] - Sim\n[2] - Sair\n'))
        if cont == 2:
            break
    elif op <= 0:
        break
print('-------------------------')
print('Obrigado por calcular! S2')
print('-------------------------')
