print('MÉDIA DE 10 VALORES')
print('*******************')
i = 1
s = 0
while i <= 10:
    valor = int(input(f'Diga o {i}º valor: '))
    s = s + valor
    i = i + 1
i = i - 1
m = s / i
print(f'A média dos valores é igual a {m}')
