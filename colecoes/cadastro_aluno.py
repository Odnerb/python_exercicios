# Algoritmo que lê uma matriz de 5 linhas por 4 colunas
# contendo informações sobre alunos de uma disciplina
# sendo todas as informações do tipo inteiro
aluno, matricula, media_provas, media_trabalhos,  nota_final = [], [], [], [], 0
melhor_aluno, maior_nota, maior_media_p = 0, 0, 0


def colegio_javali_cansado():
    print('--------------------------')
    print('|   E. E. E. F e MÉDIO   |')
    print('|     JAVALI CANSADO     |')
    print('--------------------------')
    print('Ficha de cadastro aluno: ')


for c in range(5):
    colegio_javali_cansado()
    matricula = int(input('Matrícula: '))
    for b in range(4):
        nota = int(input(f'{b+1}º NOTA BIMESTRE: '))
        media_provas.append(nota)
    print('===================')
    for trab in range(4):
        trabalho = int(input(f'{trab+1}º NOTA TRABALHO: '))
        media_trabalhos.append(trabalho)
    nota_final = (sum(media_provas) + sum(media_trabalhos)) / 4
    aluno.append([f'MATRÍCULA: {matricula}',
                  f'Média provas: {sum(media_provas)/4}',
                  f'Média trabalhos: {sum(media_trabalhos)/4}',
                  f'Nota final: {nota_final}'])
    mp = sum(media_provas) / 4
    if nota_final > maior_nota:
        maior_nota = nota_final
        melhor_aluno = matricula
        maior_media_p = mp
    elif nota_final == maior_nota and mp > maior_media_p:
        maior_media_p = mp
        melhor_aluno = matricula
    media_provas = []
    media_trabalhos = []
    nota_final = 0
print()
print('--------------')
for a in aluno:
    for media in a:
        print(media)
    print('--------------')
print()
print(f'Melhor aluno: {melhor_aluno}')









