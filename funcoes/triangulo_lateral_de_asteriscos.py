"""
Função que gera um triângulo lateral de altura 2*n-1 e n largura. Por
exemplo, a saída para n = 4 seria:

*
**
***
****
***
**
*

"""

try:
    def triangulo_lateral(n):
        qt_linhas = 2 * n - 1  # Cálcula a quantidade de linhas a serem geradas
        n_largura = n
        c = 0
        valor = 0

        for _ in range(1, qt_linhas + 1):
            if _ >= n_largura:
                if _ == n_largura:  # Assim que a linha é igual n_largura a variável
                    # valor recebe o valor de linha (_)
                    valor = valor + _
                print('*' * (valor - c))  # Em seguida passa a decrementar, imprime *
                # em ordem decrescente
                c += 1
            elif _ <= n_largura:  # Caso _ ainda não seja igual ou maior que n_largura
                # a impressão segue imprimindo o asterisco em ordem crescente.
                print('*' * _)

    linha = int(input('Quantidade de linhas: '))
    triangulo_lateral(linha)
except ValueError as e:
    print(f'Um erro inesperado ocorreu: {e}')





