"""
# print(help(print()))
def cao_latindo():
    print('Au, au , auuur')
    print('Au, au , auuur')
    print('Au, au , auuur')
cao_latindo()

def adicao(x, y):
    sum = x + y
    return sum

x = int(input('Valor de X: '))
y = int(input('Valor de Y: '))

print(adicao(x, y))
"""
r = 'Sim'
def calculadora():
    print('+_______________________________-')
    print('|     C A L C U L A D O R A     |')
    print('*_______________________________÷')
    print('Selecione o operador aritmético:')
    print('[1] + Adição')
    print('[2] - Subtração')
    print('[3] x Multiplicação')
    print('[4] ÷ Divisão')
    print('OBS: Só pode dois valores X e Y.')
while r == 'Sim' or r == 'S' or r == 'sim' or 's':
    calculadora()
    opcao = int(input('Número: '))
    x = int(input('Diga o valor de X: '))
    y = int(input('Diga o valor de Y: '))
    def adicao(x, y):
        sum = x + y
        return sum
    def subtracao(x, y):
        sub = x - y
        return sub
    def multiplicacao(x, y):
        mul = x * y
        return mul
    def divisao(x, y):
        div = x / y
        return div
    if opcao == 1:
        print(f'{adicao(x, y)}')
    elif opcao == 2:
        print(f'{subtracao(x, y)}')
    elif opcao == 3:
        print(f'{multiplicacao(x, y)}')
    elif opcao == 4:
        print(f'{divisao(x, y)}')
    else:
        print('Valor inválido!')
    r = str(input('Vai continuar? [Sim/Não]: '))

