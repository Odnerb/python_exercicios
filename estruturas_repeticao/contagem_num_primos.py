print('========================')
print('   PRIMOS ENTRE A E B   ')
print('========================')
a = int(input('Informe o valor de A: '))
b = int(input('Informe o valor de B: '))
print('-------------------------------')
cont = 0
numP = []
if a > b:
    for c in range(b, a+1):
        for i in range(1, a+1):
            if c % i == 0:
                cont = cont + 1
        if c == 2 or cont == 2:
            numP.append(c)
            cont = 0
        elif cont > 2:
            cont = 0
elif a < b:
    for c in range(a, b+1):
        for i in range(1, b+1):
            if c % i == 0:
                cont = cont + 1
        if c == 2 or cont == 2:
            numP.append(c)
            cont = 0
        elif cont > 2:
            cont = 0
print(f'A soma total dos números primos entre {a} e {b} é {sum(numP)}')
print(numP)
