print('     NOTAS DE 10 À 20    ')
print('-------------------------')
n = float(input('Informe a nota: '))
s = 0
i = 1
while (n >= 10) and (n <= 20):
    s = s + n
    i = i + 1
    n = float(input(f'Informe a {i}º nota: '))
    if (n < 10) or (n > 20):
        i = i - 1
print('------------------------------------')
print(f"""A média aritmética de todas as notas
informadas é igual a {s / i}""")
print('------------------------------------')
