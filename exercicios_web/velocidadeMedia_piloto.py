print('-----------------------')
print('VELOCIDADE MÉDIA PILOTO')
print('-----------------------')
nomePi = input('Nome do piloto: ')
dis = float(input('Distância percorrida: km'))
temp = float(input('Tempo percorrido: h'))
vm = dis/temp
text_vm = f'{vm:_.2f}'
text_vm = text_vm.replace('.',',').replace('_','.')
print('================================================')
print(f'A velocidade média do {nomePi} foi de {text_vm} km/h')
print('================================================')
