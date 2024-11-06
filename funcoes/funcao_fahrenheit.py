# Realiza a conversão de graus celsius para fahrenheit
# Fórmula:: F = C * (9/5) + 32

celsius = float(input('Cº: '))


def fahrenheit(c):
    f = c*(9/5)+32
    return f


print('Convertendo celsius para fahrenheit')
print('-----------------------------------')
print(f'Fº: {fahrenheit(celsius)}')
