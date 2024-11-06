"""
Faça um programa que receba do usuário o nome de um arquivo texto e mostre
na tela quantas linhas este arquivo possuí.
"""

print("Digite o nome do arquivo a ser criado: ")
try:
    arquivo = input()
    nome = arquivo
    with open(f"{arquivo}.txt", "w", encoding="UTF-8") as arquivo:
        print(f"O arquivo {nome} foi criado.")
        while True:
            texto = input()
            if texto != '0':
                arquivo.write(f"{texto}\n")
            else:
                break
    with open(f"{nome}.txt", "r", encoding="UTF-8") as arquivo:
        print(f' arquivo "{nome}.txt" tem')
        arquivo.seek(0)
        print(len(arquivo.readlines()))
except (OSError, IOError, TypeError, ValueError, SyntaxError, KeyboardInterrupt) as error:
    print(f"O erro encontrado: {error}")

