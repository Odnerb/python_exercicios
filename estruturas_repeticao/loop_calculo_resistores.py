print('  CALCULO RESISTORES EM  PARALELO  ')
print('-----------------------------------')
print('Digite 0 para sair-----------------')
r1, r2, tpR = 1, 1, ''
while r1 >= 1 and r2 >= 1:
    r1 = float(input('Valor de R1: '))
    r2 = float(input('Valor de R2: '))
    print('--------------------------')
    print('Selecione a opção:\n[1] - Ω\n[2] - kΩ\n[3] - mΩ')
    op = int(input(''))
    if op == 1:
        tpR = 'Ω'
    elif op == 2:
        tpR = 'kΩ'
    elif op == 3:
        tpR = 'mΩ'
    else:
        tpR = 'Não informado'
    print('==================')
    if r1 >= 1 and r2 >= 1:
        r = (r1*r2)/(r1+r2)
        print(f'R = {r:_.2f}{tpR}')
        print('==================')
    else:
        print('Você quis sair! ')
        break
print('==========================')
print('\U0001F60DObrigado por calcular!\U0001F60D')
