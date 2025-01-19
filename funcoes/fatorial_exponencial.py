"""
Função não-recursiva que recebe um número inteiro positivo n e retorna o fatorial
exponencial desse número. Um fatorial exponencial é um inteiro positivo n elevado
à potência de n - 1, que por sua vez é elevado à potência de n - 2 e assim em
diante. Ou seja:  n^(n-1).(n-2)...

"""


def fatorial_exponencial(n):
    try:
        total = 1
        for expoente in range(1, n, 1):
            if expoente+1 < n:
                total *= (expoente+1)**expoente
            else:
                total = n ** total
        return total
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == "__main__":
    print("Informe um número inteiro positivo.")
    numero = int(input("Numero: "))
    print(fatorial_exponencial(numero))

