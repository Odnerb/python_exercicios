print('-------------------------------')
print('  E S T A C I O N A M E N T O  ')
print('-------------------------------')
print('Exemplo:-----------------------')
print('Ao invés de usar 12:50 use 12_50')
hc = str(input('Hora de chegada: h'))
hp = str(input('Hora de saída: h'))
print('-------------------------------')
if int(str(hc)) < int(str(hp)):
    m = ((int(str(hp)) * 60) * 0.01) - ((int(str(hc)) * 60) * 0.01)
    h = m / 60
elif int(str(hc)) == int(str(hp)):
    h = 24
elif int(str(hp)) < int(str(hc)):
    h = (24 + (int(str(hp)) * 0.01)) - (int(str(hc)) * 0.01)
else:
    m = ((int(str(hc)) * 60) * 0.01) - ((int(str(hp)) * 60) * 0.01)
    h = m / 60
if (h >= 1) and (h <= 2):
    print('Valor a pagar: R$1,00')
elif (h >= 3) and (h <= 4):
    print('Valor a pagar R$1,40')
elif h >= 5:
    print(f'Valor a pagar R${h * 2:.2f}')
elif hp < hc and h >= 5:
    print(f'Valor a pagar R${h * 2:.2f }')
