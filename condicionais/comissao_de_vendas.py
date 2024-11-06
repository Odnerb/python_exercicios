venda = float(input('Valor da venda mensal: R$'))
print('Comissão:-----------------')
if venda >= 100_000.00:
    print(f'Total: R${(venda * (14/100)) + 700:.2f}')
elif (venda < 100_000.00) and (venda >= 80_000.00):
    print(f'Total: R${(venda * (14/100)) + 650:.2f}')
elif (venda < 80_000) and (venda >= 60_000.00):
    print(f'Total: R${(venda * (14/100)) + 600:.2f}')
elif (venda < 60_000.00) and (venda >= 40_000.00):
    print(f'Total: R${(venda * (14/100)) + 550:.2f}')
elif (venda < 40_000) and (venda >= 20_000.00):
    print(f'Total: R${(venda * (14/100)) + 500:.2f}')
else:
    print(f'Total: R${(venda * (14/100)) + 400:.2f}')
