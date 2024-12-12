"""
Função que calcula o número neperiano usando uma séria. A função deve usa como
parâmetro o número de termos que serão somados (quanto maior o número, mais
próxima a resposta estará do valor e).

"""
import math


def numero_niperiano(n):
    neperiano = math.log(n)
    return f'O número niperiano de {n} é: {neperiano:.2f}'

try:
    numero = int(input('Numero: '))
    print(numero_niperiano(numero))
except (TypeError, AttributeError, ValueError) as erro:
    print(f'Erro encontrado: {erro}')




