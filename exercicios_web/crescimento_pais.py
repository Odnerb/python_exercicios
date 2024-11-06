a = int(input('Quantidade de habitantes população A: '))
b = int(input('Quantidade de habitantes população B: '))
ano = 1
while a < b:
    a = a + (a * (3/100))
    b = b + (b * (1.5/100))
    if a >= b:
        break
    ano = ano + 1
text_a = f'{a:_.0f}'
text_b = f'{b:_.0f}'
text_a = text_a.replace('.', ',').replace('_', '.')
text_b = text_b.replace('.', ',').replace('_', '.')
print(f'Em {ano} anos a população do país A será maior que país B')
print(f'população aprox. A = {text_a} habitantes\npopulação aprox. B = {text_b} habitantes')
