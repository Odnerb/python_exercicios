din_carlos = 15000
din_joao = 5000
m = 0
while din_joao <= din_carlos:
    m = m + 1
    din_carlos = din_carlos + (din_carlos * (2/100))
    din_joao = din_joao + (din_joao * (5/100))
t_joao = f'{din_joao:_.2f}'
t_carlos = f'{din_carlos:_.2f}'
t_joao = t_joao.replace('.', ',').replace('_', '.')
t_carlos = t_carlos.replace('.', ',').replace('_', '.')
print('=================================')
print(f"""Em {m} meses João irá igualar ou
ultrapassar Carlos.\nCom o valor de:
João -> fundo renda fixa = R${t_joao}\nCarlos -> poupança = R${t_carlos}""")
