# Números A e B que leiam valores menor que 10.000
# será feito dois vetores: um irá pegar o valor dito e colocar na posição do seu algarismo correspondente.
# o outro vetor irá somar os valores de A e B, se a soma passar de 10, será diminuido 10 e somado +1 para o próximo valor lido.
vA, vB, vAlga, vAlgb, vSum, cont = [], [], [], [], [], 0
for cont in range(1, 11):
    a = float(input(f'Diga o {cont}º valor de A: '))
    print('-----------------------------------------------')
    b = float(input(f'Diga o {cont}º valor de B: '))
    print('-----------------------------------------------')
    vA.append(a)
    vB.append(b)
for c in vA:
    cont = 0
    for i in str(c):
        if i == '.':
            cont = cont + 1
        elif i != '.' and cont == 1 and int(i) != 0:
            vAlga.append(int(i))
for c in vB:
    cont = 0
    for i in str(c):
        if i == '.':
            cont = cont + 1
        elif i != '.' and cont == 1 and int(i) != 0:
            vAlgb.append(int(i))
for c in range(10):
    vSum.append(vAlga[c] + vAlgb[c])
print('-----------------------------------------------')
print(f'Algarismos de A: {vAlga}')
print(f'Algarismos de A: {vAlgb}')
print(f'Algarismos de A: {vSum}')
