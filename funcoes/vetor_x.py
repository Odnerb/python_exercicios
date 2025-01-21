"""
Função que recebe um vetor X de 30 elementos inteiros e retorna dois parâmetros,
A (contendo valores pares de X) e B (contendo valores ímpares de X).

"""

import random


def checa_elementos(vetorx):
    a, b = [], []
    a.extend([valor for valor in vetorx if valor % 2 == 0])  # Serão armazenados elementos pares
    b.extend([valor for valor in vetorx if valor % 2 == 1])  # Serão armazenados elementos ímpares
    return f"""Os valores do vetor X são: {vetorx}
- A herda pares de X: {a}
- B herda ímpares de X: {b}
"""


if __name__ == "__main__":
    random.seed(123)  # Gera random pré-definito a repetir para testes
    # vetor do tipo set, para evitar repetição de números
    X = {random.randint(1, 100) for _ in range(11)}  # X é um vetor Constante

    # O set é convertido para o tipo lista, na função checa_elementos.
    print(checa_elementos(list(X)))
