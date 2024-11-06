print('-------------------------------------')
print(' IMPOSTO SOBRE CIRCULAÇÃO MERCADORIA ')
print('-------------------------------------')
valorP = float(input('Valor da mercadoria: R$'))
print('Estados de destino do produto: [MG/SP/RJ/MS]')
estado = str(input('Qual estado? '))
if estado == 'MG' or estado == 'mg':
    impP = valorP + (valorP * (7/100))
elif estado == 'SP' or estado == 'sp':
    impP = valorP + (valorP * (12/100))
elif estado == 'RJ' or estado == 'rj':
    impP = valorP + (valorP * (15/100))
    text_imp = f'{impP:_.2f}'
elif estado == 'MS' or estado == 'ms':
    impP = valorP + (valorP * (8/100))
if estado == 'MG' or estado == 'mg' or estado == 'SP' or estado == 'sp' or estado == 'RJ' or estado == 'rj' or estado == 'MS' or estado == 'ms':
    text_valor = f'{valorP:_.2f}'
    text_valor = text_valor.replace('.', ',').replace('_', '.')
    text_imp = f'{impP:_.2f}'
    text_imp = text_imp.replace('.', ',').replace('_', '.')
    print('--------------------------------------')
    print(f'Valor do produto: R${text_valor}')
    print(f'Valor do produto com destino\npara {estado}: R${text_imp}')
    print('--------------------------------------')
else:
    print('ERRO: Digite a sigla correta\nde um dos Estados de destino!')
