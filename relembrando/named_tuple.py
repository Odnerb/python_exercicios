from collections import namedtuple

carro = namedtuple('Carro', ['marca', 'modelo', 'ano'])
fiatUno = carro(marca='FIAT', modelo='Uno', ano=2002)
print(fiatUno)
print(type(fiatUno))
print(type(carro))
