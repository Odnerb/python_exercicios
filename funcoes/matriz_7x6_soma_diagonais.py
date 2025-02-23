"""
Matriz que recebe por parâmetro, uma matriz 7 x 6 e retorna a soma dos
elementos da diagonal principal e secundária.
"""
from typing import List


print('Informar os elementos nesse formato -> 1 2 3')


def matriz(l1: str, l2: str, l3: str, l4: str, l5: str, l6: str, l7: str) -> str:
    l1: List[str] = l1.split()
    l2: List[str] = l2.split()
    l3: List[str] = l3.split()
    l4: List[str] = l4.split()
    l5: List[str] = l5.split()
    l6: List[str] = l6.split()
    l7: List[str] = l7.split()

    vetor: List[List[int]] = []
    lista1: List[int] = []
    lista2: List[int] = []
    lista3: List[int] = []
    lista4: List[int] = []
    lista5: List[int] = []
    lista6: List[int] = []
    lista7: List[int] = []

    for v1 in l1:
        lista1.append(int(v1))
    vetor.append(lista1)

    for v2 in l2:
        lista2.append(int(v2))
    vetor.append(lista2)

    for v3 in l3:
        lista3.append(int(v3))
    vetor.append(lista3)

    for v4 in l4:
        lista4.append(int(v4))
    vetor.append(lista4)

    for v5 in l5:
        lista5.append(int(v5))
    vetor.append(lista5)

    for v6 in l6:
        lista6.append(int(v6))
    vetor.append(lista6)

    for v7 in l7:
        lista7.append(int(v7))
    vetor.append(lista7)

    diagonal_principal: int = lista1[0] + lista2[1] + lista3[2] + lista4[3] + lista5[4] + lista6[5]
    diagonal_secundaria: int = lista1[5] + lista2[4] + lista3[3] + lista4[2] + lista5[1] + lista6[0]
    print('Matriz:')

    for linha in vetor:
        print(linha)

    return f'Soma da diagonal principal: {diagonal_principal}\nSoma da diagonal secundária: {diagonal_secundaria}'


if __name__ == '__main__':
    a = str(input('Informe os três primeiros elementos de A: '))
    b = str(input('Informe os três primeiros elementos de B: '))
    c = str(input('Informe os três primeiros elementos de C: '))
    d = str(input('Informe os três primeiros elementos de D: '))
    e = str(input('Informe os três primeiros elementos de E: '))
    f = str(input('Informe os três primeiros elementos de F: '))
    g = str(input('Informe os três primeiros elementos de G: '))

    try:
        print(matriz(a, b, c, d, e, f, g))

    except (ValueError, AttributeError, TypeError) as exc:
        print(f'Um erro foi encontrado: {exc}')
