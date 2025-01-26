"""
Calcula Desvio Padrão de um vetor (lista)
"""

import random
import statistics  # Biblioteca para cálculos estátisticos


def desvio_padrao(vetor):
    """
    :param vetor: recebe um vetor
    :return: o desvio padrão desse vetor
    """
    try:
        return f"{statistics.stdev(vetor):.5f}..."
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        return f"OPS: Um erro inesperado aconteceu: {exc}"


def conversao(vetor):
    """
    :param vetor: recebe um vetor digitado pelo usuário.
    :return: converte os iteráveis da lista em valores do tipo int.
    """
    valores = vetor
    vetor = []
    for valor in valores:
        if valor == "," or valor == " ":
            pass
        else:
            vetor.extend([int(valor)])
    return vetor


if __name__ == "__main__":
    # vetor = [random.randint(1, 100) for _ in range(1, 100+1)]  # testando com números aleatórios
    print("Por favor, passe os valores assim -> 1, 2, 3,... ")
    print("Ou assim -> 1 2 3,... ")
    vetor = list(input("Insira os valores: "))

    print(desvio_padrao(conversao(vetor)))

