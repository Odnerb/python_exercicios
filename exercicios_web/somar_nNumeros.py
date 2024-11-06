soma = 0
media = 0
for c in range(1, 6):
    num = int(input(f'Diga o pimeiro {c}º valor: '))
    soma = soma + num
    if c == 5:
        media = soma / c
print('================================')
print(f'A soma dos cinco números é: {soma}')
print(f'A média dos cinco números é: {media}')
print('================================')
