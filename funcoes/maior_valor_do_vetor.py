"""
Função que recebe um vetor e verifica qual interador do iterável é o maior.
"""


def maior_valor(vetor):
    """
    :param vetor: recebe uma lista de vetores com interáveis do tipo inteiro.
    :return: o maior vetor ou uma mensagem pedindo para inserir somente valores inteiros.
    """
    try:
        print(f"Todos os valores vetor: {vetor}")
        if type(max(vetor)) == int:  # verifica se o maior valor encontrado é do tipo inteiro.
            return f"Maior valor encontrado: {max(vetor)}"
        return "Insira somente valores inteiros no vetor!"
    except (AttributeError, IndexError, NameError, RecursionError, TypeError, ValueError, ZeroDivisionError) as exc:
        #  Se der erro, a execeção irá retornar o tipo de erro ocorrido.
        print(f"OPS: Um erro inesperado aconteceu: {exc}")


if __name__ == '__main__':
    lista = [1, 8, 7, 3, 4]
    print(maior_valor(lista))

