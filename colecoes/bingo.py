"""
BINGO - Gerador de cartela com números aleatórios de 0 a 99
"""

from random import randint
v, num, jogo = 0, 0, []
print('+-----------------+')
print('|  B  I  N  G  O  |')
print('+-----------------+')
qntCartela = int(input('Quantas cartelas vai querer:\n[1] - 1 Cartela\n[2] - 2 Cartelas\n[3] - 3 Cartelas\nOpção: '))
# Enquanto quantidade de cartelas não forem preenchidas "len(jogo)"
# de acordo com a quantidade específicada pelo usuário "qntCartela"
# o programa não finaliza.
while len(jogo) < qntCartela:
    cartela = set()
    while len(cartela) != 25:
        v = randint(0, 99)  # randint irá gerar um número aleatório nessa faixa e armazenar na variável "v"
        cartela.add(v)  # cartela é uma coleção do tipo conjunto, serve para armazenar os valores gerados.
    jogo.append(cartela)  # jogo é uma lista onde será armazenado os conjuntos de valores de cada cartela.
print()
print('--------------------------')
print('         Seu Jogo:        ')
print('--------------------------')
# matriz 5x5 da cartela
for _ in jogo:  # Esse loop, vai pegar cada cartela pela posição com os valores contidos.
    print('---------------------------')
    # O loop, vai pegar os números contidos no set e imprimí-los em forma de uma matriz 5x5
    for cartela in _:
        # abaixo, será gerados 5 números por linhas de acordo com as 5 colunas dividas pelo loop.
        if num == 0:
            print(f'[', end='')
        print(f'{cartela:4}', end=' ')
        num += 1
        if num == 5:
            print(f'', end=']')
            num = 0
            print()
print('--------------------------')
