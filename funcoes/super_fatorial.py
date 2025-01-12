"""
Função não-recursiva que recebe um número inteiro positivo N e retorna o
superfatorial desse número. O  superfatorial de um número N é definido pelo
produto dos N primeiros fatoriais de N. Assim, o superfatorial de 4 é:
sf(4) = 4! * 3! * 2! * 1!

"""
from funcoes.fatorial import fatorial


def superfatorial(n):
    """
    sf -> É o total do superfatorial
    :param n: recebe um valor inteiro positivo
    :return:
    """
    sf = 1  # Inicalmente começa com 1, porque fatorial de 1 é único (ele mesmo)
    for numero in range(1, n+1):
        sf *= fatorial(numero)  # todo fatorial que é chamada a função, é retornado o resultado
        # e múltiplicado pelo próximo iterador do range.
    return sf


if __name__ == "__main__":
    print(f"Informe um número inteiro positivo")
    num = int(input("Número: "))

    print(superfatorial(num))



