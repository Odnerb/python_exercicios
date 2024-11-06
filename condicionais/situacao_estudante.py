print(' ESCOLA JAVALI CANSADO ')
print('=======================')
lab = float(input('Trabalho laboratório: '))
avS = float(input('Avaliação semestral: '))
exF = float(input('Exame final: '))
media = (lab+avS+exF)/3
tx_media = f'{media:_.2f}'
tx_media = tx_media.replace('.', ',').replace('_', '.')
print('=======================')
print(f'Média aluno: {tx_media}')
if media <= 2.9:
    print('Aluno está reprovado')
elif (media >= 3) and (media <= 4.9):
    print('Aluno está em recuperação')
else:
    print('Aluno está aprovado')
print('=======================')
