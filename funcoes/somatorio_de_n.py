"""
Faça um algoritmo que receba um número inteiro positivo n e calcule o
somatório de 1 até n.

"""


def soma_range(n):
    soma = 0
    for num in range(1, n+1):
        soma = soma + num
    return f"A soma dos valores de 1 a {n} é {soma}"


try:
    numero = int(input("Diga um valor: "))
    print(soma_range(numero))

except (SyntaxError, ValueError, TypeError, StopIteration) as erro:
    print(f"Um erro foi encontrado: {erro}")
