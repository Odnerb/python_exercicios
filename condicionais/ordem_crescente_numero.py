print(' CONTAGEM CRESCENTE ')
print('--------------------')
n = int(input('Diga um número: '))
q = int(input('De quanto em quanto? '))
nf = int(input('Até que número contar? '))
print('-----------------------------------')
for n in range(n, nf+1, q):
    print(n)
