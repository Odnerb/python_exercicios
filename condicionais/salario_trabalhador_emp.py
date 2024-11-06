print('Trabalhador Brasiliero')
print('$$$$$$$$$$$$$$$$$$$$$$')
sal = float(input('Qual o salário: R$'))
emp = int(input('Quanto de empréstimo? R$'))
pSal = sal * (20/100)
if emp > pSal:
    print('Empréstimo não concedido.')
elif not emp > pSal:
    print('Empréstimo concedido.')
