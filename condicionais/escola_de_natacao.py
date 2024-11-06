print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('ESCOLA DE NATAÇÃO - PEIXE BOTO')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
nome = str(input('Insira seu nome: '))
idade = int(input('Insira sua idade: '))
print('------------------------------')
print(f'Seja bem-vindo(a) {nome}')
print(f'idade: {idade} anos')
if (idade >= 5) and (idade <= 7):
    print('Categoria: Infantil ')
elif (idade >= 8) and (idade <= 10):
    print('Categoria: Infantil B')
elif (idade >= 11) and (idade <= 13):
    print('Categoria: Juvenil A')
elif (idade >= 14) and (idade <= 17):
    print('Categoria: Juvenil B')
else:
    print('Categoria: Maiores de 18 anos')
