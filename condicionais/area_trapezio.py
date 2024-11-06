print('---------------------')
print('CÁLCULO ÁREA TRAPÉZIO')
print('---------------------')
bMaior = float(input('Digite o valor da base maior: '))
bMenor = float(input('Digite o valor da base menor: '))
alt = float(input('A altura do trapézio: '))
print('============================================')
print('[1] - cm\n[2] - m')
u = int(input('Selecione a unidade de medida utilizada: '))
if u == 1:
    uMedida = 'cm'
else:
    uMedida = 'm'
print('============================================')
if bMaior == 0 or bMenor == 0:
    print('ERRO: Nenhuma das bases podem ser igual a zero!')
else:
    aTrapezio = ((bMaior+bMenor)*alt)/2
    print(f'A área do trapézio é igual {aTrapezio}{uMedida}')
