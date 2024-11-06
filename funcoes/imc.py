def mensagem():
    print('--------- I M C ------------')
    print('- Índice de Massa Corporal -')
    print('----------------------------')


def imc(a, p):
    imc = p/(a*a)
    print('----------------------------')

    if imc <= 16:
        return f'{imc:.2f} imc --- Magreza grave'
    
    elif imc > 16 and imc <= 16.9:
        return f'{imc:.2f} imc --- Magreza moderada'

    elif imc > 16.9  and imc <= 18.5:
        return f'{imc:.2f} imc --- Magreza leve'
    
    elif imc > 18.5 and imc <= 24.9:
        return f'{imc:.2f} imc --- Peso ideal'
    
    elif imc > 24.9  and imc <= 29.9:
        return f'{imc:.2f} imc --- Sobrepeso'
    
    elif imc > 29.9 and imc <= 34.9:
        return f'{imc:.2f} imc --- Obesidade grau I'
    
    elif imc > 34.9 and imc <= 39.9:
        return f'{imc:.2f} imc --- Obesidade grau II ou severa|'
    
    return f'{imc:.2f} imc --- Obesidade grau III ou mórbida|'



def main():
    mensagem()

    altura = float(input('Informe a altura em metros (Ex: 1.75): '))
    peso = float(input('Informe o peso: (em kg) '))
    print(imc(altura, peso))

main()

