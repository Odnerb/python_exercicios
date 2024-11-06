print('E.E.F.E e Médio Javali Cansado')
print('==============================')
n1 = float(input('Nota 1º Prova: '))
n2 = float(input('Nota 2º Prova: '))
n3 = float(input('Nota 3º Prova: '))
p1 = 1
p2 = 1
p3 = 2
print('==============================')
medPond = ((p1*n1)+(p2*n2)+(p3*n3))/3
text_mp = f'{medPond:_.2f}'
text_mp = text_mp.replace('.', ',').replace('_', '.')
print(f'Média ponderada = {text_mp}')
if medPond >= 6.0:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')
print('==============================')
