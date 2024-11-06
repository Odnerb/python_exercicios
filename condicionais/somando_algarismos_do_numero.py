n = str(input('Digite um número '))
print(f'A soma dos algarismos de {n}: ')
num = 0
sum = 0
print('(',end='')
for letras in enumerate(n):
    print(f'{letras[1]}+', end='')
    num = num + int(letras[1])
    if num > 0:
        sum = sum + num
    else:
        print('Valor inválido')
print(')',end='')
print('')
print(f'Resultado: {num}')
