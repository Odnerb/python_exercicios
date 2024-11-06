"""
O algoritmo abaixo cria um arquivo e permite que o usuário possa escrever
textos no conteúdo e ainda permite que o mesmo possa ler o conteúdo contido
dentro do arquivo.

O usuário poderá escrever o tanto de linhas que quiser, porém se digitar
0 (zero) o programa fecha o arquivo.
"""
try:
    print('Digite aqui sua mensagem:')
    with open("arq.txt", "w", encoding="UTF-8") as arquivo:
        while True:
            texto = input()
            if texto != '0':
                arquivo.write(f"{texto}\n")
            else:
                break
    with open("arq.txt", "r", encoding="UTF-8") as arquivo:
        print(arquivo.read())
        arquivo.seek(0)
        tamanho = arquivo.readline()
        print(f"O arquivo contém {len(tamanho)} caracteres")
except (OSError, IOError, TypeError, ValueError, SyntaxError, KeyboardInterrupt) as erro:
    print(f'Um erro inesperado foi encontrado: {erro}')
