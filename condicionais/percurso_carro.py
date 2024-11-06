km = float(input('Distância percorrida em km: '))
l = float(input('Quantidade de litros gasolina: '))
kmL = km / l
if kmL <= 8:
    print('Venda o carro!')
elif (kmL > 8) and (kmL < 12):
    print('Econômico!')
else:
    print('Super econômico!')
