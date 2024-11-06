s = 0
for n in range(2_000_000):
    if n % 2 == 0:
        print(end='')
    elif (n % 1 == 0) and (n % n == 0):
        s = s + n
soma = f'{s:_.2f}'
soma = soma.replace('.', ',').replace('_', '.')
print('=====================================')
print(f"""A soma dos n primeiros números primos
abaixo de 2.000.000 é igual a {soma}""")
