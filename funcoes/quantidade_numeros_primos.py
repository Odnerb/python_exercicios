"""
Identificando números primos em um range de N valores.

Insira um número na variável 'valor' e veja a quantidade de números primos
encontrados na faixa de valor específicado por você.

OBS: número primo é um número que só é divisível por um e por ele mesmo.
"""

try:
    def numero_primo(valor):  # Função que verifica quantos números numa faixa de n valores são primos.
        divisores, primos = [], []  # recebe duas listas: uma de divisores inteiros e outra só com números primos.
        for numero in range(1, valor + 1):
            if numero >= 2:
                divisores = []  # toda vez que saí do loop secundário, reseta a lista para receber novos valores.
                for num in range(1, numero + 1):
                    if numero % num == 0:  # Verifica se a divisão é exata.
                        divisores.extend([num])
                        if len(divisores) == 2:  # como os números primos são divisíveis por um e por eles mesmos,
                            # o tamanho da nova lista de divisores gerada tem que ser de até 2 elementos.
                            for c in enumerate(divisores):  # tira elementos de divisores e os guarda na lista primos.
                                primos.extend(c)

        primos = list(set(primos))
        primos.pop(0)
        return f'Os números primos entre {valor} são:\n{primos}'

    n = int(input('Valor: '))
    print(numero_primo(n))
except ValueError as e:
    print(f'Um erro inesperado foi encontrado: {e}')


