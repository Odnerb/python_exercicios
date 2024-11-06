print('--------------------------------------------')
print('    PREÇO ANTIGO    |  PERCENTUAL DE AUMENTO')
print('--------------------------------------------')
print('até R$50            |           5%          ')
print('entre R$50 e R$100  |           10%         ')
print('acima de R$ 100     |           15%         ')
print('--------------------------------------------')
print('--------------------------------------------')
produto = float(input('Valor produto: R$'))
if produto > 50:
    paProd = produto + (produto * (5/100))
elif (produto > 50) and (produto <= 100):
    paProd = produto + (produto * (10/100))
else:
    paProd = produto + (produto * (15/100))

if paProd <= 80:
    print(f'Valor compra: R${paProd} (Barato)')
    print('--------------------------')
    print('Preço antigo: R$50')
    print('Preço novo: R$80')
elif (paProd > 80) and (paProd <= 120):
    print(f'Valor compra: R${paProd} (Normal)')
    print('--------------------------')
    print('Preço antigo: R$50 e R$100')
    print('Preço novo: R$80 e R$120')
elif (paProd > 120) and (paProd <= 200):
    print(f'Valor compra: R${paProd} (Caro)')
    print('--------------------------')
    print('Preço antigo: acima de R$100')
    print('Preço novo: R$120 e R$200')
else:
    print(f'Valor compra: R${paProd} (Muito caro)')
    print('--------------------------')
    print('Preço antigo: acima de R$100')
    print('Preço novo: acima de R$120')
print('--------------------------')
