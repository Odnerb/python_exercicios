n = int(input('Diga um numero (inteiro): '))
if n > 0:
    for c in range(1, n+1):
        if c % 2 == 0:
            print(c)
else:
    print('ERRO: Insira valores positivos.')
