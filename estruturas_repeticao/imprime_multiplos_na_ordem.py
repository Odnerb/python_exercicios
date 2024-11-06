n = int(input('Quantos múltiplos quer ver? '))
i = int(input('Informe o valor de i: '))
j = int(input('Informe o valor de j: '))
mi = 0
print(mi, end=', ')
for c in range(1, n-1):
    mi = i * c
    mj = j * c
    if mi != mj:
        print(mi, end=', ')
    if mi + 1 == mj:
        print(mj, end=', ')
