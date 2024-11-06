print('   SOMANDO VALORES   ')
print('=====================')
i = 1
s = 0
while i <= 10:
    valor = int(input(f'Diga o {i}º valor: '))
    i = i + 1
    s = s + valor
print(f'A soma de todos os valores é igual a {s}')
