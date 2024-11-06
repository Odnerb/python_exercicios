sal = 2000
anos = 2000 - 1995
p = 1.5/100
for ano in range(1, anos+1):
    if ano <= 2:
        sal = sal + (sal*(1.5/100))
        t_sal = f'{sal:_.2f}'
        t_sal = t_sal.replace('.', ',').replace('_', '.')
        print('===========================')
        print(f'Salário atual: R${t_sal}')
    elif ano > 2:
        p = p + (p * 2)
        sal = sal + (sal*p)
        t_sal = f'{sal:_.2f}'
        t_sal = t_sal.replace('.', ',').replace('_', '.')
        print('===========================')
        print(f'Salário atual: R${t_sal}')
