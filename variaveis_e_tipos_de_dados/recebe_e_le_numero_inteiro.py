"""
Variável que recebe um número inteiro e o imprime
"""

try:
    num = int(input("Número: "))
    print(num)
except ValueError as exc:
    print(f"Oops! Ocorreu um erro: {exc}")


