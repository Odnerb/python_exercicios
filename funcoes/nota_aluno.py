# Função que cálcula a média aritmética e ponderada das
# notas do aluno.

def aluno(calculo, lista):
    if calculo == 1:
        ma = sum(lista)/len(lista)
        return f'A média aritmética é {ma}'
    mp = ((5*lista[0])+(3*lista[1])+(2*lista[2]))/(5+3+2)
    return f'A média ponderada é {mp}'


print('  CÁLCULANDO NOTAS DE ALUNO  ')
print('=============================')
print('1 - Média Aritmética')
print('2 - Média Ponderada')
print('-----------------------------')
op = int(input('Escolha a opção calculável: '))
notas = [float(input(f'Informe {n+1}: ')) for n in range(3)]
print()
print('===========================================')
print(aluno(op, notas))
