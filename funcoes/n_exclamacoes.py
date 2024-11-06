"""
Função que recebe como parâmetro um valor inteiro e gera como saída n
linhas com pontos de exclamação, conforme o exemplo abaixo (para n=5)

imprima 5 linhas

!
!!
!!!
!!!!
"""

try:
    def exclamacao(qt_linhas):
        for _ in range(1, qt_linhas+1):
            print('!' * _)
    n_linhas = int(input('Quantidade de linhas: '))
    exclamacao(n_linhas)
except ValueError as e:
    print(f'Um erro inesperado ocorreu: {e}')



