print('=====================================')
print(' C O N S U M O   D E   E N E R G I A ')
print('=====================================')
cidade = str(input('Nome da cidade: '))
hab = int(input('Total de habitantes: '))
print('-------------------------------------')
totRes, totCom, totInd = 0, 0, 0
pessoaRes, pessoaCom, pessoaInd = 0, 0, 0
for c in range(1, hab+1):
    consumo = float(input('Total de consumo de kwh: '))
    print("""Consumidor:
    [1] - Residencial
    [2] - Comercial
    [3] - Industrial""")
    codCons = int(input('Código: '))
    if codCons == 1:
        pessoaRes = pessoaRes + 1
        totRes = totRes + consumo
    elif codCons == 2:
        pessoaCom = pessoaCom + 1
        totCom = totCom + consumo
    elif codCons == 3:
        pessoaInd = pessoaInd + 1
        totInd = totInd + consumo
    else:
        print('Valor inválido!\nTente novamente!')
    if c == (hab-1):
        break
    print('- - - - - - - - - - -')
medRes = totRes / pessoaRes
medCom = totCom / pessoaCom
medInd = totInd / pessoaInd
print('===========================================')
print(f'Total de habitantes {hab}')
print('- - - - - - - - - - - - - - - - - - - - - - -')
if totRes > totCom and totRes > totInd:
    print(f'Maior consumo diário (consumidor residencial): {totRes}')
elif totCom > totRes and totCom > totInd:
    print(f'Maior consumo diário (consumidor comercial): {totCom}')
elif totInd > totCom and totInd > totRes:
    print(f'Maior consumo diário (consumidor industrial): {totInd}')
if totRes < totCom and totRes < totInd:
    print(f'Menor consumo diário (consumidor residencial): {totRes}')
elif totCom < totRes and totCom < totInd:
    print(f'Menor consumo diário (consumidor comercial): {totCom}')
elif totInd < totCom and totInd < totRes:
    print(f'Menor consumo diário (consumidor industrial): {totInd}')
print('- - - - - - - - - - - - - - - - - - - - - - -')
print(f'Total de habitantes (Residencial): {pessoaRes}')
print(f' - A média de consumo por hab. residencial: {medRes}')
print(f'Total de habitantes (Comercial): {pessoaCom}')
print(f' - A média do consumo por hab. comercial: {medCom}')
print(f'Total de habitantes (Industrial): {pessoaInd}')
print(f' - A média do consumo por hab. industrial: {medInd}')
print('===========================================')
