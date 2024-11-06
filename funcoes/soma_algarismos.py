"""
Escreva uma função que receba um número inteiro maior que zero
e retorne a soma de todos os algarismos. Por exemplo, ao número
251 corresponderá o valor 8 (2+5+1). Se o número lido não for
maior do que zero, o programa terminará com a mensagem "número inválido."
"""


def soma_algarismos(numero):
    if int(numero) > 0:
        soma = [int(algarismo) for algarismo in numero]
        return sum(soma)
    return "Número inválido."


print('Informe um número para somar seus algarismos')
numero = input("Informe o número: ")

print(soma_algarismos(numero))

