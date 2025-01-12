"""
Calcular fatorial
"""


def fatorial(n):
    """
    :param n: recebe um número inteiro
    :return f: retorna o cálculo total do fatorial de n
    """
    try:  # Tentará executar a variável recebida, se não houver erros, retorna f (fatorial)
        n = int(n)
        f = n
        for c in range(f-1, 0, -1):
            f = f * c
        return f
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == '__main__':
    numero = input('Número inteiro: ')
    print(fatorial(numero))

