"""
Função que recebe dois parâmetros, X e Z. Irá calcular e retornar
o resultado de X^z.
"""

resultado = lambda x, z: x ** z

x = int(input('Valor: '))
z = int(input('Expoente: '))

print(f"O resultado de {x}^{z} = {resultado(x, z)}")

