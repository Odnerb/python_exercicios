print('   Calculando sequência   ')
print('--------------------------')
print('somente números acima "5"')
n = int(input('Valor de n: '))
print('[0] - Calcular soma sequêncial')
print('[1] - Subtrair pares e somar grupos')
print('[2] - Calcular soma sequencial de dois em dois')
opcao = int(input('Escolha a opção: '))
s, sb, sq = 0, 0, 0
if opcao == 0:
    for c in range(1, n+1):
        sq = sq + c
elif opcao == 1:
    for c in range(1, n):
        if c % 2 == 0 and c < 5:
            sb = c * (-1)
            s = s + sb
        elif c % 1 == 0:
            s = s + c
        if c <= n:
            sq = s + ((2*n)-1)
elif opcao == 2:
    for c in range(1, n, 2):
        s = s + c
        if c <= n:
            sq = s + ((2*n)-1)
print(f'Resultado da opção {opcao} é igual a {sq}')
