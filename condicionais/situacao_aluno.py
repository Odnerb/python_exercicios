print('===========================')
print('   ESCOLA JAVALI CANSADO   ')
print('===========================')
nota = float(input('Nota: '))
faltas = int(input('Faltas: '))
if (nota >= 9) and (nota <= 10) and (faltas <= 20):
    print('Aluno conceito nível: A')
elif (nota >= 7.5) and (nota <= 8.9) and (faltas <= 20):
    print('Aluno conceito nível: B')
elif (nota >= 5) and (nota <= 7.4) and (faltas <= 20):
    print('Aluno conceito nível: C')
elif (nota >= 4) and (nota <= 4.9) and (faltas <= 20):
    print('Aluno conceito nível: D')
elif (nota >= 0) and (nota <= 3.9) and (faltas <= 20):
    print('Aluno conceito nível: E')
elif (nota >= 9) and (nota <= 10) and (faltas >= 20):
    print('Aluno conceito nível: B')
elif (nota >= 7.5) and (nota <= 8.9) and (faltas >= 20):
    print('Aluno conceito nível: C')
elif (nota >= 5) and (nota <= 7.4) and (faltas >= 20):
    print('Aluno conceito nível: D')
elif (nota >= 4) and (nota <= 4.9) and (faltas >= 20):
    print('Aluno conceito nível: E')
elif (nota >= 0) and (nota <= 3.9) and (faltas >= 20):
    print('Aluno conceito nível: E')
