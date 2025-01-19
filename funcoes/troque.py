"""
Função que recebe duas variáveis, A e B e troca o valor delas. Onde A recebe B
e B recebe A.
"""


def troque(a, b):
    novo_a, novo_b = b, a
    return novo_a, novo_b


if __name__ == "__main__":
    print("Trocando valores de variáveis")
    a = input("Informe A: ")
    b = input("Informe B: ")

    a, b = troque(a, b)
    print("Novo A: ", a)
    print("Novo B: ", b)

    print("Deseja ver novamente, se os valores foram alterados? [S/N]")
    resposta = input("S para sim e N para não: ")

    if resposta == 'S':
        print("Meu novo A: ", a)
        print("Meu novo B: ", b)




