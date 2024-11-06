"""
Função que recebe dois números inteiros positivos por parâmetro e retorna
a soma dos N números inteiros existentes

"""


def soma_numeros_entre(n1, n2):
    try:
        soma = 0
        n1, n2 = int(n1), int(n2)

        if n1 > 0 and n2 > 0:
            if n1 < n2:
                for c in range(n1, n2+1):
                    soma += c
                return f"Somando {n1} até {n2} é igual a {soma}"
            else:
                for c in range(n2, n1+1):
                    soma += c
                return f"Somando {n2} até {n1} é igual a {soma}"
        else:
            print("\nErro! Você está passando um ou mais valores menor(es) que zero!")

    except (AttributeError, IndexError, NameError, TypeError, ValueError, ZeroDivisionError) as exc:
        return f"OPS: Um erro inesperado aconteceu: {exc}"


n1 = input('Primeiro valor: ')
n2 = input('Segundo valor: ')

print(soma_numeros_entre(n1, n2))



