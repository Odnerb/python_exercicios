print('=============================')
print('  ACHANDO NÚMERO PALÍNDROMO  ')
print('      DE TRÊS DIGITOS        ')
print('       MULTIPLICAÇÃO         ')
print('=============================')
valor = int(input('Diga um número de três digitos: '))
valorAnt, a, b, palindromo = 0, 0, 0, 0
for c in range(100, valor+1):
    for i in range(c):
        calc = c * i
        calcA = str(calc)
        if calcA == calcA[::-1] and calc > 0:
            palindromo = calc
            a, b = c, i
print(f'O maior número do cálculo de {a}x{b} = {palindromo} é palíndromo')
