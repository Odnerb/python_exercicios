n = int((input('Diga um valor: ')))
i = 0
if n > 0:
    while i <= n:
        if i % 2 != 0:
            print(i)
        i = i + 1
else:
    print('ERRO: Somente números naturais: maior que zero!')
