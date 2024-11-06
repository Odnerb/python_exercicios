resp = 'S'
while resp == 'S' or resp == 's':
    print('Qual operação você quer realizar?')
    print('[0] Adição\n[1] Subtração\n[2] Multiplicação\n[3] Divisão')
    operacao = int(input('Operação: '))
    a = int(input('Diga o primeiro valor: '))
    b = int(input('Diga o segundo valor: '))
    if operacao == 0:
        soma = a + b
        print(f'A soma de {a} + {b} é igual a {soma}')
    elif operacao == 1:
        sub = a - b
        print(f'A subtração de {a} - {b} é igual a {sub}')
    elif operacao == 2:
        mul = a * b
        print(f'A multiplicação de {a} X {b} é igual a {mul}')
    else:
        div = a / b
        print(f'A divisão de {a} / {b} é igual a {div}')
    print('--------------------------------------------')
    resp = str(input('Quer continuar? [S/N] '))
    print('--------------------------------------------')
