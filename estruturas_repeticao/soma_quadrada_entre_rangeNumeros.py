print('  1000 a 9999  ')
print('---------------')
print('Soma de dois números ao quadrado')
n1 = int(input('Diga o primeiro número: '))
n2 = int(input('Diga o segundo número: '))
for c in range(1000, 10000):
    if ((n1+n2)**2) == c:
        print(c)
