"""
Algoritmo que calcula fatorial de um número inteiro positivo
"""


def fator_primo(n):
    n = int(n)
    fatorial = n
    try:
        print(f"{n}! = ", end=" ")
        for c in range(fatorial-1, 0, -1):
            fatorial = fatorial * c
            if c != 1:
                print(f"{c} *", end=" ")
            else:
                print(f"{c} =", end=" ")
        return f"{fatorial}"
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        return f"OPS: Um erro inesperado aconteceu: {exc}"


numero = input('Número inteiro: ')

print(fator_primo(numero))
