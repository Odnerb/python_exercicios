import random
print('--------------------------')
print('    Jogo da Advinhação    ')
print('--------------------------')
print('Adivinhe o valor de X')
x = random.randint(1, 1000)
n, c = 0, 0
print('==========================')
while not x == n:
    n = int(input('Qual número é o X? '))
    if n == x:
        print('Você acertou o valor de X')
        print(f'valor de X adivinhado {x}')
        c = c + 1
        break
    elif n != x:
        print('Você errou o número!')
        print('continue tentando para sair do looping!')
        if x > n:
            print(f'DICA: O valor é maior que {n}')
            print('--------------------------')
        elif x < n:
            print(f'DICA: O valor é menor que {n}')
            print('--------------------------')
        c = c + 1
print('--------------------------')
print(f'Nº de tentativas: {c}')
print('==========================')
