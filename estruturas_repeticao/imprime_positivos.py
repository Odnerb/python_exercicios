print('-----------------------------')
print('|     SOMANDO POSITIVOS     |')
print('-----------------------------')
i = 1
s = 0
while i <= 10:
    v = int(input(f'Diga {i}º valor: '))
    if v >= 0:
        s = s + v
    i = i + 1
i = i - 1
m = s / i
print(f'A média dos valores positivos é igual a {m}')
