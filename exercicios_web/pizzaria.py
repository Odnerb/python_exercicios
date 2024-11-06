print('        PIZZARIA MONA MUR          ')
print('***********************************')
print('Cardápio---------------------------')
print('[1] - Pizza mista___________R$10,00')
print('===================================')
print('Coberturas-------------------------')
print('[1] - Queijo_________________R$1,50')
print('[2] - Presunto_______________R$1,50')
print('[3] - Banana_________________R$1,50')
print('[4] - Calabresa______________R$1,50')
print('[5] - Milho__________________R$1,50')
print('[6] - Ervilha________________R$1,50')
print('[7] - Chocolate______________R$1,50')
print('[8] - Azeitona_______________R$1,50')
print('[9] - Tomate_________________R$1,50')
print('[10]- Cogumelo_______________R$1,50')
print('[11]- Camarão________________R$1,50')
print('[12]- Cebola_________________R$1,50')
print('===================================')
print('Tulipa Chopp-----------------------')
print('[1] - Brahma_________________R$0,80')
print('[2] - Skoll__________________R$0,80')
print('[3] - Heineken_______________R$0,80')
print('[4] - Budweiser______________R$0,80')
print('***********************************')
print('===================================')
pizza = int(input('Quant. pizza: '))
cober = int(input('Quant. cobertura: '))
print('***********************************')
print('***********************************')
c = 0
totPizza = pizza * 10
sum_cober = 0
while c < cober:
    c = c + 1
    esCober = int(input(f'Escolha a {c}ª cobertura: '))
    sum_cober = sum_cober + 1.50
print('-----------------------------------')
chopp = int(input('Quant. chopp: '))
resp = str(input('Da mesma marca? [S/N]'))
if resp == 'S' or resp == 's':
    sum_chopp = chopp * 0.80
elif resp == 'N' or resp == 'n':
    c = 0
    sum_chopp = 0
    while c < chopp:
        c = c + 1
        esChopp = int(input(f'Escolha a {c}ª cobertura: '))
        sum_chopp = sum_chopp + 0.80
total = totPizza + sum_cober + sum_chopp
text_pizza = f'{totPizza:_.2f}'
text_sumcober = f'{sum_cober:_.2f}'
text_sumchopp = f'{sum_chopp:_.2f}'
text_total = f'{total:_.2f}'
text_pizza = text_pizza.replace('_','.').replace('.',',')
text_sumcober = text_sumcober.replace('_','.').replace('.',',')
text_sumchopp = text_sumchopp.replace('_','.').replace('.',',')
text_total = text_total.replace('_','.').replace('.',',')
print('===================================')
print('PEDIDO-----------------------------')
print(f'Pizza_________________R${text_pizza}')
print(f'Coberturas____________R${text_sumcober}')
print(f'Chopp_________________R${text_sumchopp}')
print(f'Total:                R${text_total}')
print('===================================')
