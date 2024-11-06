resp = 'S'
i = 1
iP = 1
sPar = 0
while resp == 'S' or resp == 's':
    n = int(input(f'Diga o {i} valor: '))
    if n % 2 == 0:
        sPar = sPar + n
        iP = iP + 1
    if iP >= 50 and n % 2 == 0:
        break
    resp = str(input('Quer continuar [S/N]? '))
    i = i + 1
i = i - 1
print(f'A soma dos {iP} números pares é igual a {sPar}')
