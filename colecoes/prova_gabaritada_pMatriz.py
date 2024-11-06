"""
O Algoritmo faz avaliação de caderno de prova de 5 alunos, onde cada prova
de determinado aluno contém um total de 50 questões. As respostas são armazenadas
de uma matriz e no final será feito um compartivo das respostas com o gabarito
preliminar com às respostas corretas, a finalidade de avlaiar a quantidade acertos
e notas dos alunos.
"""

aluno1, aluno2, aluno3, aluno4, aluno5, resultado = [], [], [], [], [], []
corretasA1, corretasA2, corretasA3, corretasA4, corretasA5, cont = 0, 0, 0, 0, 0, 0
gabarito = ['a', 'a', 'e', 'd', 'e', 'c', 'c', 'e', 'e', 'b',
            'c', 'd', 'd', 'b', 'a', 'b', 'b', 'b', 'a', 'c',
            'd', 'e', 'e', 'b', 'a', 'd', 'a', 'e', 'a', 'a',
            'd', 'e', 'd', 'b', 'b', 'a', 'c', 'a', 'b', 'e',
            'd', 'e', 'e', 'b', 'a', 'c', 'c', 'e', 'e', 'b']
print('-----------------------------------------------------')
print('Cartão de respostas de A a E:\nInsira as questões')
for aluno in range(5):
    questoes = 0
    print(f'Aluno {aluno+1}')
    while questoes < 50:
        q = str(input(f'{questoes+1}º alternativa: '))
        if q == 'a' or q == 'b' or q == 'c' or q == 'd' or q == 'e':
            if aluno == 0:
                aluno1.append(q)
            elif aluno == 1:
                aluno2.append(q)
            elif aluno == 2:
                aluno3.append(q)
            elif aluno == 3:
                aluno4.append(q)
            elif aluno == 4:
                aluno5.append(q)
            questoes += 1
        else:
            print('Valor inválido!')
        if questoes == 50:
            print()
print('-----------------------------------------------------')
print('G-A-B-A-R-I-T-O')
print('-----------------------------------------------------')
for c in range(1, 6):
    print(end='[ ')
    for _ in gabarito:
        cont += 1
        if cont <= 10 and c == 1:
            print(f'{_:2}', end=' ')
        elif (cont > 10) and cont <= 20 and c == 2:
            print(f'{_:2}', end=' ')
        elif (cont > 20) and cont <= 30 and c == 3:
            print(f'{_:2}', end=' ')
        elif (cont > 30) and cont <= 40 and c == 4:
            print(f'{_:2}', end=' ')
        elif (cont > 40) and cont <= 50 and c == 5:
            print(f'{_:2}', end=' ')
    print(end=']')
    print()
    cont = 0
print('-----------------------------------------------------')
aluno = 1
while aluno <= 5:
    corretas = 0
    for linha in gabarito:
        questoes = 0
        for questao in linha:
            if aluno == 1:
                if questao == aluno1[questoes]:
                    corretasA1 += 1
            elif aluno == 2:
                if questao == aluno2[questoes]:
                    corretasA2 += 1
            elif aluno == 3:
                if questao == aluno3[questoes]:
                    corretasA3 += 1
            elif aluno == 4:
                if questao == aluno4[questoes]:
                    corretasA4 += 1
            elif aluno == 5:
                if questao == aluno5[questoes]:
                    corretasA5 += 1
            questoes += 1
    aluno += 1
print()
print(f'Gabarito aluno 1:\n{aluno1}\nTotal de acertos: {corretasA1}')
print('-----------------------------------------------------')
print(f'Gabarito aluno 2:\n{aluno2}\nTotal de acertos: {corretasA2}')
print('-----------------------------------------------------')
print(f'Gabarito aluno 3:\n{aluno3}\nTotal de acertos: {corretasA3}')
print('-----------------------------------------------------')
print(f'Gabarito aluno 4:\n{aluno4}\nTotal de acertos: {corretasA4}')
print('-----------------------------------------------------')
print(f'Gabarito aluno 5:\n{aluno5}\nTotal de acertos: {corretasA5}')
# Ajeitar código para parecer uma matriz de gabarito 5x10
