print('----------------------------------')
print('|       LANCHONETE DO CHICO       |')
print('----------------------------------')
print('| Especificação | Código | Preço |')
print('----------------------------------')
print('|Cachorro Quente|  100   |  1,20 |')
print('|Bauru Simples  |  101   |  1,30 |')
print('|Bauru com Ovo  |  102   |  1,50 |')
print('|Hamburguer     |  103   |  1,20 |')
print('|Cheeseburguer  |  104   |  1,70 |')
print('|Suco           |  105   |  2,20 |')
print('|Refrigerante   |  106   |  1,00 |')
print('----------------------------------')
pd = [0, 100, 101, 102, 103, 104, 105, 106]
totV = 0
quant = int(input('Quantidade de pedidos: '))
for c in range(1, quant+1):
    pd[c] = int(input(f'Selecione o {c}º pedido: '))
    if pd[c] == 100:
        totV = totV + 1.20
    elif pd[c] == 101:
        totV = totV + 1.30
    elif pd[c] == 102:
        totV = totV + 1.50
    elif pd[c] == 103:
        totV = totV + 1.20
    elif pd[c] == 104:
        totV = totV + 1.70
    elif pd[c] == 105:
        totV = totV + 2.20
    elif pd[c] == 106:
        totV = totV + 1.00
    else:
        print('ERRO: Insira o código correto.')
text_tot = f'{totV:.2f}'
text_tot = text_tot.replace('.', ',')
print('----------------------------------')
print(f'Total: R${text_tot}')
print('----------------------------------')
