"""
Função que recebe dois valores númericos e um símbolo (+, -, *, /)
o símbolo irá apontar a operação de cálculo a ser feita. Só valores
inteiros.
"""


def calculo(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b


def main():
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    op = input('Operador: ')
    print(calculo(a, b, op))


main()



