print('-------------------------')
print("    CHIQUINHO HOST'S     ")
print('-------------------------')
sal = float(input('Insira o seu salário: R$'))
tempS = int(input('Tempo de serviço: '))
print('-------------------------')
print('Selecione (1) para meses e (2) para anos')
confT = int(input('Meses[1] ou Anos[2]: '))
print('-------------------------')
if confT == 1 and tempS > 12:
    print('ERRO: Insira em anos (e não acrescente os meses, só valores inteiros),\ncaso seja mais de 12 meses')
elif confT == 1 and tempS <= 12:
    if sal <= 500:
        nSal = sal + (sal * (25/100))
        print(f'Salário: R${nSal}')
        print('Sem bonús')
elif confT == 2:
    if (sal > 0) and (sal <= 500) and tempS == 1:
        nSal = sal + (sal * (25/100))
        print(f'Salário: R${nSal}')
        print('Sem bonús')
    elif (sal > 0) and (sal <= 1000) and (tempS > 1) and (tempS <= 3):
        nSal = sal + (sal * (20/100))
        print(f'Salário: R${nSal}')
        print(f'Mais R$100,00 de bonús R${nSal+100}')
    elif (sal > 0) and (sal <= 1500) and (tempS > 3) and (tempS <= 6):
        nSal = sal + (sal * (15/100))
        print(f'Salário: R${nSal}')
        print(f'Mais R$200,00 de bonús R${nSal+200}')
    elif (sal > 0) and (sal <= 2000) and (tempS > 6) and (tempS <= 10):
        nSal = sal + (sal * (10/100))
        print(f'Salário: R${nSal}')
        print(f'Mais R$300,00 de bonús R${nSal+300}')
    else:
        print(f'Salário (sem reajuste): R${sal}')
        print(f'Mais R$500,00 de bonús R${sal+500}')
