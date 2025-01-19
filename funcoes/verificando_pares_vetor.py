"""
Função que recebe um vetor de inteiros e retorna quantos valores pares possuí.
"""


def verifica_vetor(vetor):
    """
    :param vetor: recebe a lista de valores
    :var pares: retorna a lista com os valores pares de vetor
    :return: uma lista de valores pares encontrados no vetor
    """
    pares = [par for par in vetor if par % 2 == 0]
    return f"Os valores pares do vetor são: {pares}"


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(verifica_vetor(lista))





