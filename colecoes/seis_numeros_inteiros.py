vetP, vetI = [], []
for c in range(0, 6):
    n = int(input(f'{c+1}º valor: '))
    if n % 2 == 0:
        vetP.append(n)
    else:
        vetI.append(n)
print('=-=-=-=-=-=-=-==-=-=-==-=-==-=-=')
print(f'Vetor par: {vetP}')
print(f'Soma vet. par: {sum(vetP)}')
print(f'Vetor impar: {vetI}')
print(f'Qnt de impares: {len(vetI)}')
