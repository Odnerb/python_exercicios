# Algoritmo que lê uma matriz de 5 linhas por 4 colunas
# contendo informações sobre alunos de uma disciplina
# sendo todas as informações do tipo inteiro


aluno: list = []
matricula: int = 0
media_provas: list = []
media_trabalhos: list = []
nota_final: float = 0


def colegio_javali_cansado() -> None:
    print('--------------------------')
    print('|   E. E. E. F e MÉDIO   |')
    print('|     JAVALI CANSADO     |')
    print('--------------------------')
    print('Ficha de cadastro aluno: ')


for c in range(5):
    colegio_javali_cansado()
    matricula = int(input('Matrícula: '))

    for b in range(4):
        nota = float(input(f'{b+1}º NOTA BIMESTRE: '))
        media_provas.append(nota)
    print('===================')

    for trab in range(4):
        trabalho = float(input(f'{trab+1}º NOTA TRABALHO: '))
        media_trabalhos.append(trabalho)

    nota_final = ((sum(media_provas)/4) + (sum(media_trabalhos)/4)) / 2
    aluno.append({'Matrícula': matricula,
                  'Média provas': sum(media_provas)/4,
                  'Média trabalhos': sum(media_trabalhos)/4,
                  'Nota final': nota_final})

    media_provas = []
    media_trabalhos = []
    nota_final = 0

if __name__ == "__main__":
    melhor_aluno: int = 0
    pior_aluno: int = 0
    maior_media: float = 0
    menor_media: float = 10

    print('-------------------------------------------------------------------')
    for dicionario in aluno:
        if dicionario['Nota final'] > maior_media:
            maior_media = dicionario['Nota final']
            melhor_aluno = dicionario['Matrícula']
        elif dicionario['Nota final'] < menor_media:
            menor_media = dicionario['Nota final']
            pior_aluno = dicionario['Matrícula']

    print(f'O melhor aluno foi o aluno {melhor_aluno} com média {maior_media}')
    print(f'O pior aluno foi o aluno {pior_aluno} com média {menor_media}')
    print('-------------------------------------------------------------------')
    print(aluno)
    print()
