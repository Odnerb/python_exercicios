print('   Validador de número primo   ')
print('===============================')
continuar = 's'
while continuar == 's':
    if continuar == 'n':
        print('Obrigado por usar a ferramenta!')
        break
    elif continuar == 's':
        num = int(input('Diga o número: '))
        if num > 1:
            if num % 2 == 0:
                print(f'Número {num} não é primo!')
            elif (num % 1 == 0) and (num % num == 0):
                print(f'Número {num} é primo!')
        else:
            print('insira um número maior que 1')
    continuar = str(input('Quer continuar? [s/n]\n'))
