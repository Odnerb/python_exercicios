# Função que recebe altura e raio de um cilindro circular
# e retorna o volume do cilindro.

def vol_cilindro(a, r):
    v = 3.141592 * (r**2) * a
    return v


print('   VOLUME DO CILINDRO  ')
print('-_-_-_-_-_-_-_-_-_-_-_-')
print('Forneça os dados abaixo.')
altura = float(input('Altura: '))
raio = float(input('Raio: '))
print('-----------------------')
print(f'Volume: {vol_cilindro(altura, raio)}')
