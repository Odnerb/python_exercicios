"""
Função que retorna o maior fator primo de um número
- Exemplo: o maior fator primo de 630 é 7
- Fatores primos são todos os números que divisíveis
por um determinado número, quando multiplicados, retornam
este mesmo número. A múltiplicação dos fatores primos de 630
tornam ele novamente.

630 | 2
315 | 3
105 | 3
 35 | 5
  7 | 7  <- Maior fator primo da decomposição de 630
  1 |
"""


def fator_primo(n):
    n = int(n)
    try:
        fatores = []
        quociente = n
        for c in range(2, n+1):
            while quociente % c == 0:
                fatores.append(c)
                quociente = quociente / c
        return f"O maior fator primo de {n} é {max(fatores)}"
    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        return f"OPS: Um erro inesperado aconteceu: {exc}"


if __name__ == '__main__':
    numero = input('Número inteiro: ')

    print(fator_primo(numero))
