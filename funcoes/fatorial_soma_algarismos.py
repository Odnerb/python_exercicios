# Importando módulo que eu mesmo criei
from funcoes import soma_algarismos


def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num - 1)


if __name__ == '__main__':
    numero = int(input('Diga o número, calcule o fatorial e some os algarismos: '))

    total = soma_algarismos.soma_algarismos(str(fatorial(numero)))
    print(f'A soma de {fatorial(numero)} é igual a {total}')

