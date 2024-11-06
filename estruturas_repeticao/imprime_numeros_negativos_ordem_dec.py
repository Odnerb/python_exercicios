n = int(input('Diga um número (inteiro negativo): '))
if n > 0:
    for c in range(n, 0, -1):
        if c % 2 == 1:
            print(c)
else:
    print('ERRO: Insira valores inteiros negativos')