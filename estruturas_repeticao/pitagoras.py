print('  TEOREMA DE PITAGÓRICO  ')
print('        no loop          ')
print('-------------------------')
i = 0
for a in range(0, 1001):
    for b in range(0, a):
        for c in range(0, b):
            s = (a**2)+(b**2)+(c**2)
            if s == 1000 and i == 0:
                print(f'{a}²+{b}²+{c}² = 1000')
                i = i + 1
            elif i == 1:
                break
