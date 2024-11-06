print('^^^^^^^^^^^^^^^^^^^^')
print('     TRIÂNGULOS     ')
print('------3 lados-------')
print('^^^^^^^^^^^^^^^^^^^^')
a = int(input('Diga o valor de A: '))
b = int(input('Diga o valor de B: '))
c = int(input('Diga o valor de C: '))
print('-----------------------')
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print('Triângulo equilátero')
    elif ((a > b and a == c) or (a > c and a == b)) or ((b > a and b == c) or (b == a and b > c)):
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')
else:
    print('Não é um triângulo!')
print('-----------------------')

