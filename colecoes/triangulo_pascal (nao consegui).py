# Escrevendo programa que lê um número inteiro positivo n e em seguida
# imprima n linhas do chamado Triângulo de Pascal:

tp = int(input('Diga um número para formar o Triângulo de Pascal: '))
sum = 0
for c in range(1, 2):
    print()
    for i in range(1, tp+1):
        if c == i:
            print(f'{c} {i}')
            sum = c + 1
        else:
            print(f'{c} {sum} {c}')
            sum = sum + c

