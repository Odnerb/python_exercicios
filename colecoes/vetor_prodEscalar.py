conjA, conjB, prodEsc = [], [], []
print('Conjunto A')
for c in range(0, 5):
    x1 = float(input(f'{c+1}º valor: '))
    conjA.append(x1)
print('Conjunto B')
for c in range(0, 5):
    y2 = float(input(f'{c+1}º valor: '))
    conjB.append(y2)
for c in range(0, 5):
    calc = conjA[c] * conjB[c]
    prodEsc.append(calc)
print('-----------------------------------')
print(f'Conjunto A: {conjA}')
print(f'Conjunto B: {conjB}')
print(f'Produto Escalar: {sum(prodEsc):.2f}')
print('-----------------------------------')
