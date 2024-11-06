print('      IMPAR OU PAR       ')
print('-------------------------')
qnt = int(input('Quantos números irá ler? '))
par, impar = 0, 0
for i in range(1, qnt+1):
    v = int(input(f'Informe o {i}º valor: '))
    if v != 1000:
        if v % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
    elif v == 1000:
        par = par + 1
        break
print('-------------------------')
print(f'Total de pares: {par}')
print(f'Total de impares: {impar}')
print(f'Total de valores lidos: {par + impar}')
print('-------------------------')
