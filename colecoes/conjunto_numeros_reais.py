print(' CONJUNTOS DOS NÚMEROS REAIS ')
print('=============================')
c, conjQ, quadQ = 10, [], []
for i in range(1, c+1):
    q = float(input('Diga um número real: '))
    conjQ.append(q)
    quadQ.append(q**2)
print(f'Elementos primeiro vetor: {conjQ}')
print(f'Elementos segundo vetor: {quadQ}')
