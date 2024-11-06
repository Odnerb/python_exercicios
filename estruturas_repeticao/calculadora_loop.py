print('   CALCULADORA MATEMÁTICA   ')
print('++++++++++++++++++++++++++++')
print('Escolha a opção:------------')
print('[1] - Adição')
print('[2] - Subtração')
print('[3] - Multiplicação')
print('[4] - Divisão')
print('[5] - Sair')
print('----------------------------')
op = 0
while not op == 5:
    op = int(input('Selecione a operação: '))
    print('--------------------------------------')
    if (op >= 1) and (op <= 4):
        n1 = int(input('Diga o primeiro número: '))
        n2 = int(input('Diga o segundo número: '))
        if op == 1:
            c = n1 + n2
            print(f'{n1} + {n2} = {c}')
        elif op == 2:
            c = n1 - n2
            print(f'{n1} - {n2} = {c}')
        elif op == 3:
            c = n1 * n2
            print(f'{n1} x {n2} = {c}')
        elif op == 4:
            c = n1 / n2
            print(f'{n1} ÷ {n2} = {c}')
    elif op == 5:
        print('----------------------')
        print('Obrigado por calcular!')
        print('----------------------')
        break
    else:
        print('Por favor! Insira a opção correta.')

