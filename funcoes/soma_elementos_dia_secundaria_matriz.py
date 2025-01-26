def matriz(m):
    """
    :param m: recebe uma matriz de tamanho 3 x 3.
    :return: o somatório dos valores da diagonal secundária.
    """
    try:
        print("Valores acima da diagonal principal: valores")
        return f"A soma dos elementos acima da diagonal principal é: {sum([m[0][1], m[0][2], m[1][2]])}"
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == "__main__":
    mz = [[15, 10, 1],
          [99, 3, 5],
          [7, 4, 100]]

    print(matriz(mz))

