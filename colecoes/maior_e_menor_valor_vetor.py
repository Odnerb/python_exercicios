print('================================')
print('= Maior e menor valor da lista =')
print('================================')
valores = []
for c in range(1, 11):
    v = int(input(f'Diga o {c}º valor da lista: '))
    valores.append(v)
print('================================')
print(f'O maior valor da lista é: {max(valores)}')
print(f'O menor valor da lista é: {min(valores)}')
