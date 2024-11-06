print(' FAIXA ETÁRIA ')
print('-_-_-_-_-_-_-_-')
nome = str(input('Qual o seu nome?\n'))
dataNas = int(input('Em que ano você nasceu?\n'))
idade = 2023 - dataNas
print('------------------------')
print(f'Nome: {nome}\nidade: {idade} anos')
if idade < 5:
    print('Você ainda é um bebê!')
elif idade >= 5 and idade <= 13:
    print('Você é uma criança!')
elif idade > 13 and idade < 18:
    print('Você é um adolescente!')
elif idade >= 18 and idade < 60:
    print('Você é adulto(a)!')
else:
    print('Você é idoso(a)!')
print('------------------------')