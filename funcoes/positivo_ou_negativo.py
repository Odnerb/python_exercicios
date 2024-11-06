# Algoritmo que retorna 1 para números positivos, -1 para negativos
# caso a entrada seja 0 o retorno será 0.

num = float(input('Número: '))


def positivo_ou_negativo():
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0


print(positivo_ou_negativo())
