print('======================')
print('   ESCOLA ASNOS PRÓ   ')
print('======================')
bim = 0
media = 0
n1 = float(input('Nota 1ºBimestre: '))
n2 = float(input('Nota 2ºBimestre: '))
media = (n1 + n2) / 2
print('============================')
if ((n1 < 0) or (n1 > 10)) or ((n2 < 0) or (n2 > 10)):
    print('Notas inválidas')
else:
    print(f'Média do aluno: {media}')
print('============================')
