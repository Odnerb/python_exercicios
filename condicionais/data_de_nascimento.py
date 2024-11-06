dia = int(input('Insira o dia em que nasceu: '))
mes = int(input('Insira o mês em que nasceu: '))
ano = int(input('Insira o ano em que nasceu: '))
print('---------------------------------------')
if (mes > 0) and (mes < 13):
    if ano <= 2023:
        if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0:
            if dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                print('Data válida')
            elif dia <= 30 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
                print('Data válida')
            elif dia <= 29 and mes == 2:
                print('Data válida')
            else:
                print('Data inválida')
        else:
            if dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                print('Data válida')
            elif dia <= 30 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
                print('Data válida')
            elif dia <= 28 and mes == 2:
                print('Data válida')
            else:
                print('Data inválida')
    else:
        print('Data inválida')
else:
    print('Data inválida')
