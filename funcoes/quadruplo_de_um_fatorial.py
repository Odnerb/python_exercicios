"""
Função não-recursiva que recebe um número inteiro positivo n e retorne o
fatorial quádruplo desse número. O fatorial quádruplo de um número n é dado por:
(2n)!/n!

"""

from funcoes.fatorial import fatorial


def quadruplo_fatorial(n):
    """
    :param n: parâmetro n recebe um número inteiro positivo
    :return:
    """
    try:
        qf = (fatorial(2 * n))/fatorial(n)
        return qf
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == "__main__":
    print(f"Insira um número inteiro positivo")
    num = int(input(f"Número: "))
    print(quadruplo_fatorial(num))




