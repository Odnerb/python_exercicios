print('------------------------')
print('    I      M      C     ')
print('------------------------')
p = float(input('Peso: kg'))
a = float(input('Altura: m'))
imc = p/(a**2)
print(f'Indíce de Massa Corporal: {imc:.2f}')
if (imc > 0) and (imc <= 18.5):
    print('Abaixo do peso')
elif (imc > 18.5) and (imc <= 24.9):
    print('Saudável')
elif (imc > 24.9) and (imc <= 29.9):
    print('Peso em excesso')
elif (imc > 29.9) and (imc <= 34.9):
    print('Obesidade Grau I')
elif (imc > 34.9) and (imc <= 39.9):
    print('Obesidade Grau II (severa)')
else:
    print('Obesidade Grau III (mórbida)')
print('------------------------')
