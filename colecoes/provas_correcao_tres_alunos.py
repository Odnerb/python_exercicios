"""
Algortimo que faz a correção das provas de três alunos de acordo com gabarito.
No final retorna a nota de cada aluno.
"""
gabarito = ['a', 'b', 'c', 'e', 'c', 'd', 'd', 'b', 'e', 'a']
respostas, aluno_nota = [], []
aluno = {}
matricula, nota, i, prova = 0, 0, 0, []
for c in range(3):
    matricula = int(input(f'Aluno {c+1}° matrícula: '))
    for q in range(10):
        questao = str(input(f'{q+1}º questão alternativa: '))
        prova.append(questao)
    aluno.update({matricula: prova})
    prova = []
    print('----------------------------------------------------')
for matricula in aluno:
    print('==============================================')
    print(f'Aluno matrícula: {matricula}')
    print(f'Respostas: {aluno[matricula]}')
    respostas = aluno[matricula]
    for c in range(10):
        if gabarito[c] == respostas[c]:
            nota += 1
    aluno_nota.append(nota)
    nota = 0
    print(f'Nota do aluno: {aluno_nota[i]}')
    if aluno_nota[i] < 7:
        print('Recuperação')
    else:
        print('Aprovado')
    print('==============================================')
    print()
    i += 1
print('----------------------------------------------------')
print(f'GABARITO: {gabarito}')
print('----------------------------------------------------')
