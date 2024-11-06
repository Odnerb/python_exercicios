v = int(input('Informe um número: '))
print('------------------------------')
s = 0
for i in range(1, v+1):
    if (v % i == 0) and (not v == i):
        s = s + i
        print(f'{i} é divisor de {v}')
print(f"""A soma de todos os divisores
de {v} é igual a {s}""")
