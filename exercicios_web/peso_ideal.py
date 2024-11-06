h = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
sexo = str(input('Digite o seu sexo: [M/F] '))
print('============================')
if sexo == 'M' or sexo == 'm':
    pesoIdeal = (72.7 * h) - 58
    print(f'Peso ideal: {pesoIdeal}')
elif sexo == 'F' or sexo == 'f':
    pesoIdeal = (62.1 * h) - 44.7
    print(f'Peso ideal: {pesoIdeal}')
print('============================')
