"""
Matriz que recebe por parâmetro, uma matriz 3 x 3 e retorna a soma dos
elementos da diagonal principal e secundária.
"""
from typing import List


print('Informar os elementos nesse formato -> 1 2 3')


def matriz(l1: str, l2: str, l3: str) -> str:
    l1: List[str] = l1.split()
    l2: List[str] = l2.split()
    l3: List[str] = l3.split()

    vetor: List[List[int]] = []
    lista1: List[int] = []
    lista2: List[int] = []
    lista3: List[int] = []

    for v1 in l1:
        lista1.append(int(v1))
    vetor.append(lista1)

    for v2 in l2:
        lista2.append(int(v2))
    vetor.append(lista2)

    for v3 in l3:
        lista3.append(int(v3))
    vetor.append(lista3)

    diagonal_principal: int = lista1[0] + lista2[1] + lista3[2]
    diagonal_secundaria: int = lista1[2] + lista2[1] + lista3[0]
    print('Matriz:')

    for linha in vetor:
        print(linha)

    return f'Soma da diagonal principal: {diagonal_principal}\nSoma da diagonal secundária: {diagonal_secundaria}'


if __name__ == '__main__':
    a = str(input('Informe os três primeiros elementos de A: '))
    b = str(input('Informe os três primeiros elementos de B: '))
    c = str(input('Informe os três primeiros elementos de C: '))

    try:
        print(matriz(a, b, c))

    except (ValueError, AttributeError, TypeError) as exc:
        print(f'Um erro foi encontrado: {exc}')




