c = 1
num, numP = [], []
v = float(input(f'Diga o {c}º valor: '))
num.append(v)
while v != 0:
    c = c + 1
    v = float(input(f'Diga o {c}º valor: '))
    num.append(v)
    if v % 2 == 0:
        numP.append(v)
num.remove(0)
print('====================================')
print(f'A soma dos valores: {sum(num)}')
print(f'A quant. de números digitados: {len(num)}')
print(f'A média dos números digitados: {sum(num)/len(num)}')
print(f'O maior número digitado: {max(num)}')
print(f'O menor número digitado: {min(num)}')
print(f'A média dos números pares: {sum(numP)/len(numP)}')
