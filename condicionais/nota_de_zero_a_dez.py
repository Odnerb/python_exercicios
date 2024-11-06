print('---------------------')
print('   NOTA DE 0 A 10    ')
print('---------------------')
nota = 0
while nota < 1 or nota > 10:
    nota = float(input('Diga uma nota de 0 a 10: '))
    if (nota >= 1) and (nota <= 10):
        print(f'Nota: {nota}')
    elif (nota <= 0) or (nota >= 11):
        print('ERRO: Valor inválido!')
