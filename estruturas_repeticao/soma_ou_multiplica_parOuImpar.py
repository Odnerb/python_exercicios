totP, totM, totSum, totMul = 0, 1, 0, 1
for i in range(1, 11):
    v = float(input(f'Diga o {i} valor: '))
    if v % 2 == 0:
        totP = totP + v
    else:
        totM = totM * v
    totSum = totSum + v
    totMul = totMul * v
print('----------------------------------------------')
print(f'A soma dos pares: {totP:.0f}')
print(f'A multiplicação: {totM:.0f}')
print('----------------------------------------------')
print(f'A soma total dos valores: {totSum:.0f}')
print(f'A multiplicação do total dos valores: {totMul:.0f}')
print('----------------------------------------------')
