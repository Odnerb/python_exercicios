"""
Função que recebe a distância em km e a quantidade de litros de gasolina
consumidos por um carro em um percurso. Calcula o consumo em km/l e
retorna uma mensagem de acordo com a tabela abaixo.

|  Consumo | (km/l) |    MENSAGEM     |
|----------|--------|-----------------|
| Menor que|    8   |   Venda carro   |
| Entre    | 8 e 14 |    Econômico    |
| Maior que|   12   | Super econômico |
"""

d = float(input('Distância percorrida (em km): '))
l = float(input('Quantidade de litros consumidos (em l): '))


consumo = lambda x, y: x / y
resultado = consumo(d, l)


print(f'Foram consumidos {resultado:.2f} km/l')
