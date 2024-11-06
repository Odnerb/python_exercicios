"""
Faça um programa que receba do usuário o nome de um arquivo texto e mostre
na tela quantas letras são vogais e quantas são consoantes.
"""

print("Digite o nome do arquivo a ser criado: ")
try:
    arquivo = input()
    nome = arquivo
    vogais, consoantes = [], []
    with open(f"{arquivo}.txt", "w", encoding="UTF-8") as arquivo:
        print(f"O arquivo {nome} foi criado.")
        for c in nome:
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                vogais.append(c)
            else:
                consoantes.append(c)
        print(f' arquivo "{nome}.txt" tem')
        print(f"{len(vogais)} vogais: {vogais}")
        print(f"{len(consoantes)} consoantes: {consoantes}")
except (OSError, IOError, TypeError, ValueError, SyntaxError, KeyboardInterrupt) as error:
    print(f"O erro encontrado: {error}")
