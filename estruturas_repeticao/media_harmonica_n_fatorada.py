n = int(input('Diga um número: '))
f = 1
somaDf = 0
if n > 0:
    for i in range(1, n+1):
        for j in range(1, i):
            if f == 0:
                f = i * j
            elif f != 0:
                f = f * j
            elif i == j:
                f = 1
        df = 1/f
        somaDf = somaDf + df
        f = 0
else:
    print('ERRO: Insira valores inteiros acima de 0!')
e = n / somaDf
print(f'O resultado da média harmônica de {n} é {e}')
