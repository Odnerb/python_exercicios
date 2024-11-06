print('   SOMANDO VALORES DE UM VETOR   ')
print('=================================')
print('Diga qualquer valor inteiro')
valores = []
for i in range(1, 9):
    valor = int(input(f'{i}º número: '))
    valores.append(valor)
print('=======================================')
print(f'Todos os valores da lista:\n{valores}')
print('- - - - - - - - - - - - - - - - - - - -')
print('Quais valores da lista quer calcular?')
for i in range(1, 3):
    posicao = int(input('Posição: '))
    for c, valor in enumerate(valores):
        if posicao == c and i == 1:
            a = valor
            print(f'Primeiro valor escolhido: {valor}')
        elif posicao == c and i == 2:
            b = valor
            print(f'Segundo valor escolhido: {valor}')
sum = a + b
print(f'A soma dos valores {a} + {b} = {sum}')
