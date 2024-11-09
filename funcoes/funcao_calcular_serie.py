"""
Faça uma função que receba um inteiro N como parâmetro, calcule o
resultado da seguinte série:

S = 2/4 + 5/5 + 10/6 + ... + (N² + 1) / (N + 3)

"""


def serie(n):
    for num in range(1, n+1):
        valor = ((num**2)+1)/(num+3)
        print(f"{valor:.2f}")


try:
    numero = int(input("Diga um valor: "))
    serie(numero)

except (SyntaxError, ValueError, TypeError, StopIteration) as erro:
    print(f"Um erro foi encontrado: {erro}")

