print('===========================')
print('= ESCOLA MULAS SEM CABEÇA =')
print('===========================')
print('Notas das provas dos alunos')
notas = []
for c in range(1, 16):
    a = float(input(f'{c}º Nota: '))
    notas.append(a)
print('===========================')
print(f'Média da turma: {sum(notas)/len(notas)}')
