print('=============================')
print('  SOMANDO TAMANHO DE LETRAS  ')
print('---------DE NÚMEROS----------')
print('=============================')
print('Digite qualquer número em letras')
s = 0
num = str(input('Número: '))
s = s + len(num)
while num != 'mil':
    num = str(input('Número: '))
    s = s + len(num)
print(f"""A soma de todos os valores digitados
é igual a {s}""")
