print('  ACHANDO MÚLTIPLOS DE UM NÚMERO  ')
print('       -OS DEZ PRIMEIROS-         ')
print('==================================')
vetor = []
x = int(input(f'Diga o número: '))
for c in range(1, 11):
    m = x * c
    vetor.append(m)
print('==================================')
print(f'Múltiplos de M({x}) = {set(vetor)}...')
