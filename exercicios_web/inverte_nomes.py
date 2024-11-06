print('-----------------')
print('Inversor de nomes')
print("""veja a quantidade
de letras e se seu nome é
um Palíndromo.
OBS: DIGITE SOMENTE O SEU PRIMEIRO NOME EM MINÚSCULO""")
print('-----------------')
nome = str(input('Digite seu nome: '))
print('---------------------------------')
print(f'O inverso do seu nome é: {nome[::-1]}')
print(f'seu nome possuí {nome.__len__()} letras')
pali = nome[::-1]

if nome == pali:
    print('Seu nome é um Palíndromo')
else:
    print('Seu nome não é Palíndromo')
print('---------------------------------')
