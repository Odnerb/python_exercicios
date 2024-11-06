print('---------------------------')
print('       F   I   A   T       ')
print('c o n c e s s i o n á r i a')
print('---------------------------')
print('Custo de fábrica-----------')
cFab = float(input('Valor do carro: R$'))
print('---------------------------')
if cFab <= 12_000:
    custoF = cFab + (cFab*(5/100))
elif (cFab > 12_000) and (cFab <= 25_000):
    custoF = cFab + (cFab * (10/100)) + (cFab * (15/100))
else:
    custoF = cFab + (cFab * (15/100)) + (cFab * (20/100))
consumidor = f'{custoF:_.2f}'
consumidor = consumidor.replace('.', ',').replace('_', '.')
print(f'Consumidor final: R${consumidor}')
