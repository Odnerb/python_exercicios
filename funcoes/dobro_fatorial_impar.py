"""
Algoritmo que calcula fatorial de um número inteiro positivo impar
"""


def fator_primo(n):
    try:
        n = int(n)
        fatorial = n
        if n % 2 == 1:
            for c in range(1, fatorial-1, 2):
                fatorial = fatorial * c
                if c != 1:
                    print(f"{c} *", end=" ")
                else:
                    print(f"{c} *", end=" ")
            print(f"{n}", end=" = ")
            return f"{fatorial}"
        else:
            return "Só é aceito números inteiros impares positivos!"

    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == '__main__':
    numero = input('Número inteiro: ')
    print(fator_primo(numero))

