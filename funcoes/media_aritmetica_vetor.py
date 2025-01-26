"""
Calcula a média aritmética de um v (lista) e imprime ele ao inverso.
"""

import statistics  # Biblioteca para cálculos estátisticos


def desvio_padrao(v):
    """
    :param v: recebe um vetor.
    :return: um texto com os resultados ao inverter e de média do vetor.
    """
    try:
        return f"""Vetor: {v}\nInverso: {v[::-1]}\nMédia vetor: {statistics.mean(v)}""".ljust(0)
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        return f"OPS: Um erro inesperado aconteceu: {exc}"


def conversao(v):
    """
    :param v: recebe um vetor digitado pelo usuário.
    :return: converte os iteráveis da lista em valores do tipo int.
    """
    valores = v
    v = []
    for valor in valores:
        if valor == "," or valor == " ":
            pass
        else:
            v.extend([int(valor)])
    return v


if __name__ == "__main__":
    print("Por favor, passe os valores assim -> 1, 2, 3,... ")
    print("Ou assim -> 1 2 3,... ")
    vetor = list(input("Insira os valores: "))

    print(desvio_padrao(conversao(vetor)))
