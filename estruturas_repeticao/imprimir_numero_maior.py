print('Preencha os campos abaixo')
print('-------------------------')
qt = int(input('Quantos números irá comparar? '))
m, v = 0, 0
for i in range(1, qt+1):
    num = float(input(f'Informe o º{i} número: '))
    if num > m:
        m = num
    if m == num:
        v = v + 1
print('-------------------------')
print(f'O maior número é: {m}')
print(f'E foi lido: {v} vezes')
print('-------------------------')
