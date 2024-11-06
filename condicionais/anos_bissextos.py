print('   ANO BISSEXTO   ')
print('==================')
ano = int(input('Digite o ano: '))
print('=================================')
if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
print('=================================')
