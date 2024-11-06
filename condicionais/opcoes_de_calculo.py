print('Escolha a opção:')
print('1 - A soma de dois números')
print('2 - Diferença entre 2 números (maior pelo menor).')
print('3 - Produto entre 2 números')
print('4 - Divisão entre 2 números (o denominador não pode ser zero)')
opcao = int(input('Opção: '))
if opcao == 1:
    n1 = int(input('Diga um valor: '))
    n2 = int(input('Diga outro valor: '))
    print('--------------------------')
    print(f'{n1} + {n2} = {n1 + n2}')
elif opcao == 2:
    n1 = int(input('Diga um valor: '))
    n2 = int(input('Diga outro valor: '))
    print('--------------------------')
    if n1 > n2:
        print('--------------------------')
        print(f'{n1} - {n2} = {n1 - n2}')
    else:
        print('--------------------------')
        print(f'{n2} - {n1} = {n2 - n1}')
elif opcao == 3:
    n1 = int(input('Diga um valor: '))
    n2 = int(input('Diga outro valor: '))
    print(f'{n1} X {n2} = {n1 * n2}')
elif opcao == 4:
    n1 = int(input('Diga um valor: '))
    n2 = int(input('Diga outro valor: '))
    if n2 == 0:
        print('--------------------------')
        print('O denominador não pode ser zero')
    else:
        print('--------------------------')
        print(f'{n1} e {n2} = {n1 / n2}')
else:
    print('--------------------------')
    print('Valor inválido.\nTente novamente!')
    print('--------------------------')
