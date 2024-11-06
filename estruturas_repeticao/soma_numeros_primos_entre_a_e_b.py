print('========================')
print('   PRIMOS ENTRE A E B   ')
print('========================')
a = int(input('Informe o valor de A: '))
b = int(input('Informe o valor de B: '))
cont = 0
numP = []
if a > b:
    for c in range(b, a):
        for i in range(1, a):
            if c % i == 0:
                cont = cont + 1
        if c == 2 or cont == 2:
            numP.append(c)
            cont = 0
        elif cont > 2:
            cont = 0
elif a < b:
    for c in range(a, b):
        for i in range(1, b):
            if c % i == 0:
                cont = cont + 1
        if c == 2 or cont == 2:
            numP.append(c)
            cont = 0
        elif cont > 2:
            cont = 0
print('----------------------------------')
print(f'Entre {a} e {b}')
print(f'Total: {len(numP)} números primos')
print('----------------------------------')
