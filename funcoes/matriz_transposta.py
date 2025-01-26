"""
Função que recebe uma matriz quadrada de ordem N e calcula a sua transposta
(se B é a matriz transposta de A então aij=bji).
"""


def matriz_transposta(*m):
    """
    :param m: recebe uma matriz de qualquer tamanho.
    :return: a transposta da matriz.
    """
    try:
        transposta = list(map(lambda *i: [j for j in i], *m))
        return transposta
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == "__main__":
    a = [[15, 10, 1],
         [99, 3, 5],
         [7, 4, 100]]

    print(matriz_transposta(*a))

