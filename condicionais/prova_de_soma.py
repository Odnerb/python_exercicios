print('---------------------')
print(' PROVA DE MATEMÁTICA ')
print('Valendo: 5 Pontos')
print('---------------------')
q1 = int(input('Qual a soma de 10 + 85? '))
q2 = int(input('Qual a soma de 93 + 17? '))
q3 = int(input('Qual a soma de 99 + 8? '))
q4 = int(input('Qual a soma de 37 + 12? '))
q5 = int(input('Qual a soma de 11 + 17? '))
s = 0
q = [q1, q2, q3, q4, q5]
print('---------------------')
for c in range(0, 5):
    print(q[c])
    if q[c] == (10+85):
        s = s + 1
    elif q[c] == (93+17):
        s = s + 1
    elif q[c] == (99+8):
        s = s + 1
    elif q[c] == (37+12):
        s = s + 1
    elif q[c] == (11+17):
        s = s + 1
print(f'Nota: {s}')
print('---------------------')
