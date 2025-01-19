"""
Função não-recursiva que recebe um número inteiro positivo n e retorna o
hiperfatorial desse número. O hiperfatorial de um número n, escrito H(n) e
definido por:
H(n) = 1¹.2².3².4⁴.5⁵...nⁿ

"""


def hiper_fatorial(n):
    try:
        hf = n ** n
        for numero in range(n-1, 0, -1):
            hf *= (numero ** numero)
        return hf
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == "__main__":
    print("Informe um número inteiro positivo.")
    numero = int(input("Numero: "))
    print(hiper_fatorial(numero))

