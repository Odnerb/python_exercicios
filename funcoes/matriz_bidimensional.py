"""
Função que recebe uma matrix 4 x 4 e retorna quantos valores maiores que 10
ela possuí.
"""


def matriz(m):
    """
    :param m: recebe uma matriz de tamanho 4 x 4.
    :return: a quantidade de valores maiores que 10 e os valores encontrados.
    """
    try:
        valores = []
        for lista in m:
            valores.extend([item for item in lista if item > 10])
        return f"Existem valores {len(valores)} maiores que 10: {valores}"
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == "__main__":
    mz = [[15], [10], [1], [8],
          [99], [3], [5], [6],
          [7], [4], [100], [0]]

    print(matriz(mz))



