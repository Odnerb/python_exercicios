"""
Algoritmo que calcula fatorial de um número inteiro positivo
"""


def fator_primo(n):
    try:
        n = int(n)
        fatorial = n
        print(f"{n}! = ", end=f" {n} * ")
        for c in range(fatorial-1, 0, -1):
            fatorial = fatorial * c
            if c != 1:
                print(f"{c} *", end=" ")
            else:
                print(f"{c} =", end=" ")
        return f"{fatorial}"
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == '__main__':
    numero = input('Número inteiro: ')
    print(fator_primo(numero))
