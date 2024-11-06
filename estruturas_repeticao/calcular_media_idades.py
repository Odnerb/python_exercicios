i, c, idades = 1, 1, 0
while i >= 1:
    i = int(input(f'Diga a {c}ª idade: '))
    if i > 0:
        idades = idades + i
        c = c + 1
    elif i == 0:
        c = c - 1
        break
    elif i < 0:
        print('Inválido')
print('---------------------------------------')
print(f'A média de idades é igual a {idades/c}')
print('---------------------------------------')
