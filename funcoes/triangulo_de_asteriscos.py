"""
Função que gera um triângulo de altura 2*n-1 e n largura. Por
exemplo, a saída para n = 4 seria:

          *
         ***
        *****
       *******
      *********
     ***********

"""

try:
    def triangulo(n):
        qt_linhas = 2 * n - 1  # Cálcula a quantidade de linhas a serem geradas
        n_largura = n

        for _ in range(1, qt_linhas + 1, 2):
            print(end=' ' * n_largura)
            print('*' * _)
            n_largura = n_largura - 1

    l = int(input('Quantidade de linhas: '))
    triangulo(l)
except ValueError as e:
    print(f'Um erro inesperado ocorreu: {e}')

