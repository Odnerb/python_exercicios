n = int(input('Diga um número para calcular somar de 1 até ele: '))
sum = 0
for c in range(0, n+1):
    sum = sum + c
print(f'A soma de todos os valores é igual a {sum}')
