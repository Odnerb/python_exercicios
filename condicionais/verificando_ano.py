print('----------------------')
print('    VALIDANDO ANOS    ')
print('----------------------')
dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Digite o ano: '))
print('=================================')
if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0:
    if (mes >= 1) and (mes <= 12):
        if ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)) and ((dia >= 1) and (dia <= 30)):
            print(f'O ano {ano} é bissexto!')
        elif ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)) and ((dia >= 1) and (dia <= 31)):
            print(f'O ano {ano} é bissexto!')
        elif (mes == 2) and (dia >= 1) and (dia <= 29):
            print(f'O ano {ano} é bissexto!')
        else:
            print(f'O ano {ano} não possui esse dia!')
    else:
        print(f'O ano {ano} não possui esse dia!')
else:
    if (mes >= 1) and (mes <= 12):
        if ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)) and ((dia >= 1) and (dia <= 30)):
            print(f'O ano {ano} não é bissexto!')
        elif ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)) and ((dia >= 1) and (dia <= 31)):
            print(f'O ano {ano} não é bissexto!')
        elif (mes == 2) and (dia >= 1) and (dia <= 28):
            print(f'O ano {ano} não é bissexto!')
        else:
            print(f'O ano {ano} não possui esse dia!')
    else:
        print(f'O ano {ano} não possui esse dia!')
print('=================================')
