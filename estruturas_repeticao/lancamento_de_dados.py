print('   Lançamento de dados    ')
print('--------------------------')
print('  Operadores relacionais  ')
n = int(input('Quantas vezes irá comparar: '))
for c in range(1, n+1):
    d1 = int(input('Valor de d1: '))
    d2 = int(input('Valor de d2: '))
    print('------------------------------')
    if (d1 > 0 and d2 > 0) and (d1 <= 6 and d2 <= 6):
        if d1 > d2:
            print(f'O dado {d1} é maior que o dado {d2}.')
        elif d2 > d1:
            print(f'O dado {d2} é maior que o dado {d1}.')
        else:
            print(f'Ambos os dados são iguais.')
    else:
        print('ERRO: Recomece.')
        print('Insira os valores certos dos dados!')
        break
    print('------------------------------')
