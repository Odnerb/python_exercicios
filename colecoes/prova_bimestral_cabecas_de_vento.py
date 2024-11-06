# Algotimo de matriz 10x3, onde lê as notas de alunos em três provas.
# O objetivo deste algoritmo é encontrar o aluno com a pior nota.
count = 1
aluno = [[10, 9, 8], [5, 3, 7], [1, 0, 8.5],
         [2, 0, 0], [1.5, 1.5, 9.5], [10, 5, 7.8],
         [10, 10, 10], [4.75, 10, 7], [10, 10, 4.5],
         [7, 7, 7]]
pior_prova = []
pior_nota = 10
pior_media = 0
pior_aluno = 0
for a in aluno:
    print('----------------------------')
    print(f'Aluno {count}')
    print(f'Nota - 1ºBIMESTRE {a[0]}\n'
          f'Nota - 2ºBIMESTRE {a[1]}\n'
          f'Nota - 3ºBIMESTRE {a[2]}\n')
    count += 1
for contador in range(3):
    pior_nota = 10
    for c, a in enumerate(aluno):
        # Condicional if armazena o aluno com pior nota e media... mas...
        if a[contador] < pior_nota:
            pior_nota = a[contador]
            pior_media = sum(a)/len(a)
            pior_aluno = c + 1
        # Caso um ou mais alunos possuam as piores notas iguais, o critério de desempate
        #   será feito pela variavel de pior_media
        elif a[contador] == pior_nota:
            if sum(a)/len(a) < pior_media:
                pior_media = sum(a)/len(a)
                pior_nota = a[contador]
                pior_aluno = c + 1
    pior_prova.append([f'{contador+1}º BIMESTRE', f'Aluno {pior_aluno}', f'Pior nota: {pior_nota}'])
for pior in pior_prova:
    print(f'Pior prova', pior)
