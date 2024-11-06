"""
# LISTAS - relembrando

listaCompras = ['Banana', 'Pêra', 'Morango', 'Açaí', 'Melância', 'Kiwi', 'Uvas']
print(listaCompras)
listaCompras.append('Berijela')
listaCompras.pop(7)
listaCompras.sort()
listaCompras.extend(['Graviola', 'Caqui', 'Ingá', 'Beterraba', 'Salmão'])
listaCompras.sort()
listaCompras.pop(2)
listaCompras.pop(9)
print(listaCompras)

lc = []
lc = lc + listaCompras
listaCompras.clear()
print(lc)
print(listaCompras)

Transforma toda string separada por espaço, em um elemento na lista.
carnes = 'Patinho Coxão-Mole Rabada Linguiça Toscana Contra-Filé Frango Costela'
carnes = carnes.split()
print(carnes)
print(type(carnes))

Transformando lista em string
# carnes = ' '.join(carnes)
# print(carnes)

for carne in carnes:
    print(carne)
i = 0
while i < len(carnes):
    print(carnes[i], end=' ')
    i = i + 1
print()
exibir = carnes.index('Contra-Filé')
print(exibir)

for index, carne in enumerate(carnes):
    print(index, carne)

carnes.reverse()
print(carnes)
carnes.sort()
print(carnes)

grupoCarnes = carnes.copy()
grupoCarnes.extend(['Alcatra', 'Carne-Moida', 'Peito-de-Frango', 'Salsicha'])
print(grupoCarnes)
print(carnes)
grupoCarnes.sort()
print(grupoCarnes)

print('AÇOUGUE')
print('===================')
for carne in grupoCarnes:
    print(carne)



# TUPLAS

tvs = 'SBT', 'Record', 'Globo', 'Band', 'Rede TV', 'AmazonSat', 'Boas-Novas'
print(type(tvs))

for emissora in tvs:
    print(emissora)

umAdez = tuple(range(1, 10))
print(umAdez)

um, dois, tres, quatro, cinco, seis, sete, oito, nove = umAdez
print(um)
print(dois)
print(tres)
print(quatro)
print(cinco)
print(seis)
print(sete)
print(oito)
print(nove)

print(sum(umAdez), max(umAdez), min(umAdez), len(umAdez))

televisao = tvs + umAdez
print(televisao)

escola = tuple('São Luiz')
print(escola)

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

for mes in meses:
    print(mes)

tupla = meses
print(tupla)

nova = (1, 2, 3)
nova = nova + tupla
print(nova)

print(nova[::-1])



# DICIONÁRIOS

americaDosul = {'BR': 'BRASIL',
                'AR': 'ARGENTINA',
                'GF': 'GUIANA FRANCESA',
                'GU': 'GUIANA',
                'VE': 'VENEZUELA',
                'BO': 'BOLÍVIA',
                'CO': 'COLÔMBIA',
                'CH': 'CHILE',
                'EQ': 'EQUADOR',
                'PE': 'PERU',
                'UR': 'URUGUAI',
                'SU': 'SURINAME'}

print(americaDosul)
print(americaDosul.get('BR'))

pais = americaDosul.get('BR')

if pais:
    print(f'Encontrado o país')
else:
    print(f'País não encontrado')

print('RU' in americaDosul)
print('EA' in americaDosul)
print('BR' in americaDosul)
print('AR' in americaDosul)

locais = {(35.669075097523184, 139.7743256071043): 'Hotel Keihan Tsukiji Ginza Grande',
          (36.409770663147796, 25.463914444093692): 'Santorini',
          (37.447195520493665, 140.19203432500234): 'Fukushima',
          (8.709157360991677, 98.41333557524463): 'Khao Phing Kan',
          (16.900907813320746, -99.87747006672076): 'Acapulco',
          (19.6675664551579, -155.9971780726985): 'Kailua',
          (20.120880176567145, -155.57359098547437): 'Kukuihaele'}
print(locais)

salario = {'Jan': 12500, 'Fev': 11950, 'Mar': 13000, 'Abr': 18000}
salario['Mai'] = 17777
salario.update({'Jun': 18005})
print(salario)

ret = salario.pop('Jan')

del salario['Fev']
print(salario)

carrinho = []

produto1 = {'Nome': 'God Of War', 'Quantidade': 1, 'Valor': 125.50}
produto2 = {'Nome': 'Resident Evil 4 - Remake', 'Quantidade': 1, 'Valor': 120.00}
produto3 = {'Nome': 'PlayStation 5', 'Quantidade': 1, 'Valor': 12499.99}

carrinho.append(produto1)
print(carrinho)
carrinho.append(produto3)
print(carrinho)
carrinho.append(produto2)
print(carrinho)

v1 = produto1['Valor']
v2 = produto2['Valor']
v3 = produto3['Valor']
total = v1 + v2 + v3
print(total)

for produto, valor in produto1.items():
    print(f'{produto}: {valor}')

print(dir(produto1))



# CONJUNTOS

n = {1, 2, 3, 4, 5, 7, 7, 8, 9, 9, 9, 10, 10.0}
print(n)

if 3 in n:
    print('Tem o número 3')
else:
    print('Não tem o número 3')

print(set('Brendo Saraiva'))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 7, 10, 0]
lista.sort()
print(set(lista))

valores = {'Carro', True, 18.99, 25, -150}

for valor in valores:
    print(valor)

cidades = ['Belo Horizonte', 'Manaus', 'Porto Velho', 'Porto Velho', 'Porto Velho', 'Seringueiras', 'São Paulo', 'Cuiabá']
cidades = set(cidades)

cidades.add('Minas Gerais')

cidades.remove('Minas Gerais')
cidades.discard('Filipinas')
for cidade in cidades:
    print(cidade)

Lembre-se!!! Deep Copy
citys = cidades.copy()
citys.add('New York')
print(citys)
print(cidades)

Lembre-se!!! Shalow Copy
citys = cidades
citys.add('New York')
print(citys)
print(cidades)

cidades.clear()
print(f'{citys}\n{cidades}')


estudantes_java = {'Rodrigues', 'Padilha', 'Filepina', 'Jéssica', 'Deltan', 'Messi'}
estudantes_python = {'Pepe', 'Cristiano', 'Messi', 'Padilha', 'Deltan'}

"Só estudantes de um único curso"
so_python = estudantes_java.difference(estudantes_python)
print(so_python)

so_java = estudantes_python.difference(estudantes_java)
print(so_java)


"Estudantes em ambos"
ambos = estudantes_java & estudantes_python
print(ambos)

"Únicos"
unicos = estudantes_python | estudantes_java
print(unicos)

valores = {1, 2, 57, 99, 125.22, 0.55, -1_000_000_000_000}
print(sum(valores))
print(min(valores))
print(max(valores))
print(len(valores))
print((sum(valores))/len(valores))



# COUNTER

from colecoes import Counter

lista = [1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 7, 8]
res = Counter(lista)
print(res)
print(type(res))

print(Counter('Brendo Saraiva'))
"""

from collections import Counter

texto = """There are many variations of passages of Lorem Ipsum available,
but the majority have suffered alteration in some form, by injected humour,
or randomised words which don't look even slightly believable. If you are
going to use a passage of Lorem Ipsum, you need to be sure there isn't
anything embarrassing hidden in the middle of text. All the Lorem Ipsum
generators on the Internet tend to repeat predefined chunks as necessary,
making this the first true generator on the Internet. It uses a dictionary
of over 200 Latin words, combined with a handful of model sentence
structures, to generate Lorem Ipsum which looks reasonable. The generated 
Lorem Ipsum is therefore always free from repetition, injected humour, or
non-characteristic words etc."""

palavras = texto.split()
print(palavras)

p = Counter(palavras)
print(p)

print(len(palavras))

print(p.most_common(1))
