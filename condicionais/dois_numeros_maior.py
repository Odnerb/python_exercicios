print('Qual número é maior?')
print('===================================')
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
print('===================================')
if a > b:
    print(f'O valor A ({a}) é maior que B ({b})')
    print(f'A diferença de A e B é igual a {a - b}')
elif b > a:
    print(f'O valor de B ({b}) é maior que A ({a})')
    print(f'A diferença de B e A é igual a {b - a}')
else:
    print('ERRO: Valor inválido!')
print('===================================')
