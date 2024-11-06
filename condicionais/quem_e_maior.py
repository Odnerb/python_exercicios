a = int(input('Diga um valor para A: '))
b = int(input('Diga outro valor para B: '))
print('=====================================')
if a > b:
    print('O valor de A é maior que o valor de B')
    print(f'A = {a}\nB = {b}')
elif b > a:
    print('O valor de B é maior que o valor de A')
    print(f'A = {a}\nB = {b}')
else:
    print('Números iguais.')
print('=====================================')
