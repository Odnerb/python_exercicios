"""
Função que recebe um vetor de reais e retorna a média.
"""


def maior_valor(vetor):
    try:
        print(f"Todos os valores vetor: {vetor}")
        return f"A média vetor: {sum(vetor) / len(vetor)}"
    except (AttributeError, IndexError, NameError, RecursionError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        print(f"OPS: Um erro inesperado aconteceu: {exc}")


if __name__ == '__main__':
    notas = [7.5, 8.9, 10, 5]
    print(maior_valor(notas))

