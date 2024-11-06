print('  ÁREA DO TRIÂNGULO  ')
print('=====================')
b, h, tp = 0, 0, 3
while (b <= 0 or h <= 0) and (tp > 2 or tp <= 0):
    b = float(input('base: '))
    h = float(input('Altura: '))
    a = (b * h) / 2
    text_a = f'{a:_.2f}'
    text_a = text_a.replace('.', ',').replace('_', '.')
    print('=====================')
    print('Selecione a opção: ')
    tp = int(input('[1] - cm\n[2] - m\n'))
    print('=====================')
    if b <= 0 or h <= 0:
        print('ERRO: Insira valores acima de 0.')
    else:
        if tp == 1:
            print(f'A área do triângulo é: {text_a}cm²')
        elif tp == 2:
            print(f'A área do triângulo é: {text_a}m²')
        else:
            print(f'ERRO: Selecione 1 para cm e 2 para m')

