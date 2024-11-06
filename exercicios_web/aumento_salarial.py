print('EMPRESA CHIQUINHO STYLUS')
print('------------------------')
print('  - Aumento salarial -  ')
print('------------------------')
nomeF = str(input('Nome completo do funcionário:\n'))
cargaT = int(input('Carga horária (h): '))
salHora = float(input('valor hora (R$): '))
filhos = int(input('Quantidade de filhos: '))
perFi = 0
c = 1
while c <= filhos:
    perFi = perFi + (3/100)
    c = c + 1
sal = ((cargaT * salHora) * (313/12)) * perFi
funSal = ((cargaT * salHora) * (313/12)) + sal
text_funSal = f'{funSal:_.2f}'
text_funSal = text_funSal.replace('.',',').replace('_','.')
print('=======================================')
print(f'Funcionário(a): {nomeF}')
print(f'Salário: R${text_funSal}')
print('=======================================')
