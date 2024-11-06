# Criar função que receba como parâmetro um número inteiro
# e devolva o seu dobro.

"""Se você inserir número quebrado, o algoritmo
irá converter para um valor inteiro..."""

n = float(input('Número: '))
n = int(n)


def numero(num):
    return num * 2


print(f'O dobro de {n} é {numero(n)}')
