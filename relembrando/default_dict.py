from collections import defaultdict

personagem = defaultdict(lambda: 'Unknow')
personagem['Nome1'] = 'Brendo Saraiva'

print(personagem)
print(personagem['Nome1'])
print(personagem['Nome2'])
print(personagem)
