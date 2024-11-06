# Função que recebe a data atual (dia, mês e ano em inteiro)
# e exibe na tela no formato textual por extenso. Exemplo:
# Data: 05/04/2020
# Imprimir: 1 de janeiro de 2000

meses = ['janeiro', 'fevereiro', 'março', 'abril',
         'maio', 'junho', 'julho', 'agosto',
         'setembro', 'outubro', 'novembro', 'dezembro']

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))


def calendario(d, m, a):
    return f'{d} de {meses[m-1]} de {a}'


print(f'A data é {calendario(dia, mes, ano)}')
