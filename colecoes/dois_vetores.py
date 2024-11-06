# lendo dois vetores: reais e inteiros
vetReal = []
vetInt = []
print('-----------------------------------')
print('     VETORES: REAL E INTEIRO       ')
print('-----------------------------------')
print('[0]-Sair\n[1]-Ordem direta\n[2]-Ordem inversa\n')
opcao = int(input('Escolha a opção: '))
if opcao == 0:
    print('Fim')
elif opcao == 1 or opcao == 2:
    for c in range(1, 3):
        if c == 1:
            print('Vetor com valores reais')
        elif c == 2:
            print('Vetor com valores inteiros')
        for i in range(1, 6):
            if c == 1:
                val = float(input(f'Diga o {i}º valor: '))
                vetReal.append(val)
            elif c == 2:
                val = int(input(f'Diga o {i}º valor: '))
                vetInt.append(val)
    if opcao == 1:
        print(f'=======================================')
        print(f'Lista de reais: {vetReal}')
        print(f'Lista de inteiros: {vetInt}')
    if opcao == 2:
        print(f'=======================================')
        print(f'Lista de reais: {vetReal[::-1]}')
        print(f'Lista de inteiros: {vetInt[::-1]}')
else:
    print(f'Valor inválido!')
