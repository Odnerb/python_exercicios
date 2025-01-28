"""
Função que verifica se é um matriz identidade.

Matriz identidade, é uma matriz onde a diagonal principal é composta por números
1, e os elementos tanto acima e abaixo dela são 0.
"""


def checa_matriz(m):
    """
    :param m: recebe uma matriz de qualquer tamanho.
    :return: a transposta da matriz.
    """
    try:
        total = 0
        for linha in m:
            # Verifica se a quantidade de linhas é a mesma de colunas, pois se não for...
            if len(linha) == len(m):
                total_zeros = 0
                for elemento in linha:
                    if elemento == 1:
                        total += 1
                        if total == len(m):
                            return f"A matriz é identidade"
                    elif elemento == 0:
                        total_zeros += 1
                    else:
                        return "Não é uma matriz identidade"
            # Não será uma matriz quadrática.
            else:
                return "Não é uma matriz quadrada!"
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == "__main__":
    a = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]

    print(checa_matriz(a))
