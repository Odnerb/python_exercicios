valor = 0
maior = 0
for c in range(1, 6):
    num = int(input(f'Diga o {c}º número: '))
    if num > valor:
        maior = num
    elif valor > maior:
        maior = valor
    valor = num
print(f'O maior número digitado foi: {maior}')
