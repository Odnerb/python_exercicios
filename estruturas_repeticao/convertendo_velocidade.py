print('     CONVERSOR DE VELOCIDADE    ')
print('------------km/h; m/s-----------')
vezes = int(input('Quantas vezes quer converter? '))
print('==========================================')
v = 1
while v <= vezes:
    print('Selecione o número da opção: ')
    print('[1] - km/h --> m/s')
    print('[2] - m/s --> km/h')
    op = int(input('Opção: '))
    velo = float(input('Informe a velocidade: '))
    if op == 1:
        ms = velo * 1000
        print(f'{ms} m/s')
        print('---------------')
    elif op == 2:
        km = velo / 1000
        print(f'{km} km/h')
        print('---------------')
    else:
        print('OPÇÃO INVÁLIDA!')
    if v == vezes:
        continuar = str(input('Quer continuar? [Sim/Não]'))
        if continuar == 'Sim':
            vezes = int(input('Quantas vezes quer converter? '))
            v = 0
        else:
            break
    v = v + 1
