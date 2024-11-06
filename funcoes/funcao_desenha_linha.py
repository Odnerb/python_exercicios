"""
Função chamada desenha_linha(), onde recebe um valor e desenha a linha de
'=' a quantidade de vezes que for exigida.
"""
linha = int(input('Quantidade de linhas: '))


def desenha_linha(quantidade):
    return f"{quantidade * '='}"


print(desenha_linha(linha))
