nomeF = str(input('Nome funcionário: '))
salV = float(input('Salário: R$'))
vendas = int(input('Total em vendas: R$'))
p = int(input('Percentual das vendas: '))
totV = salV + (vendas * (p/100))
print('---------------------------------')
print('Vendedor(a): %s', nomeF)
print('Salário mensal: R$ {0}' .format(totV))
print('---------------------------------')
