print('==================')
print('  DIAS DA SEMANA  ')
print('==================')
print('[1] Segunda-feira')
print('[2] Terça-feira')
print('[3] Quarta-feira')
print('[4] Quinta-feira')
print('[5] Sexta-feira')
print('[6] Sábado')
print('[7] Domingo')
print('==========================')
print('==========================')
x = int(input('Escolha um dia de 1 a 7: '))
if x == 1:
    print('Segunda-feira')
elif x == 2:
    print('Terça-feira')
elif x == 3:
    print('Quarta-feira')
elif x == 4:
    print('Quinta-feira')
elif x == 5:
    print('Sexta-feira')
elif x == 6:
    print('Sábado')
elif x == 7:
    print('Domingo')
else:
    print('Valor inválido')
