# Algoritmo que verifica se um número é um quadrado perfeito

num = float(input('Número: '))


def quadrado_perfeito(n):
    numero = n ** 2
    if numero > 0 and numero - int(numero) == 0:
        return 'quadrado perfeito não negativo'
    return 'número decimal não perfeito negativo'


print(quadrado_perfeito(num))

