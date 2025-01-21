"""
Função que recebe um range de valores e gera um vetor contendo vários valores
inteiros e aleatórios sem repetição.
"""

import random


def vetor_aleatorio(inicio, fim):
    try:
        valores = {random.randint(inicio, fim) for _ in range(inicio, fim+1)}
        return list(valores)
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == "__main__":
    print("Gerando lista aleatória de valores")
    i = int(input("Início: "))
    f = int(input("Fim: "))

    print(vetor_aleatorio(i, f))



