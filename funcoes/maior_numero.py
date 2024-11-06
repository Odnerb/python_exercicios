# Função que recebe dois numeros e retorna o maior

def maior_numero(x, y):
    if x > y:
        return f'O número {x} é maior que {y}!'
    return f'O número {y} é maior que {x}!'


print(' MAIOR DOS NÚMEROS ')
print('-------------------')
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
print()
print('---------------------------------------------')
print(maior_numero(n1, n2))
