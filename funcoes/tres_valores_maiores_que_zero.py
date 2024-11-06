"""
O programa recebe três valores (obrigatoriamente maiores que zero), onde
irão representar as medidas dos triângulos. E determinará os triângulos
como: equilatero, isósceles e escaleno

Tipos de triângulos: https://mundoeducacao.uol.com.br/matematica/triangulos

"""


def triangulo(a, b, c):
    if (a+b > c) and (b+c > a) and (a+c > b):
        print('-----------------------------')
        print('É um triângulo', end=' ')
        if a == b and b == c:
            return f'equilátero'
        elif (a == b and c % a) or (b == c and a % c) or (a == c and b % c):
            return 'isósceles'
        return 'escaleno'
    else:
        return 'Não é um Triângulo'


def main():
    a = float(input('Primeiro lado (cm): '))
    b = float(input('Segundo lado (cm): '))
    c = float(input('Terceiro lado (cm): '))

    return triangulo(a, b, c)


print(main())
