print('+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+')
print('  OPERAÇÕES MATEMÁTICAS BÁSICAS  ')
print('+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+')
print('[1] - Adição\n[2] - SUBTRAÇÃO\n[3] - Multiplicação\n[4] - Divisão')
op = int(input('Escolha a operação matemática: '))
if (op > 0) and (op <= 4):
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))
else:
    print('ERRO: Insira os valores correspondentes às operações!')
if op == 1:
    text_op = 'soma'
    operacao = n1 + n2
elif op == 2:
    text_op = 'subtração'
    operacao = n1 - n2
elif op == 3:
    text_op = 'multiplicação'
    operacao = n1 * n2
elif op == 4:
    text_op = 'divisão'
    if n1 % n2 == 0:
        operacao = n1 // n2
    else:
        operacao = n1 / n2
if (op > 0) and (op <= 4):
    print(f'A {text_op} de {n1} e {n2} é igual a {operacao}')
