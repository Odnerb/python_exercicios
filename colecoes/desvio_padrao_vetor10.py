from typing import List

v: List[float] = []
vDP: List[float] = []
vetor: List[float] = []

for c in range(0, 10):
    n = float(input(f'Diga o {c+1}º número: '))
    v.append(n)

vetorN = v
m = sum(v)/len(v)

for c, va in enumerate(v):
    vDP.append(va-m)

for c, v in enumerate(vDP):
    vetor.append(v**2)
dp = sum(vetor)/len(vetor)

if __name__ == '__main__':
    print('======================================')
    print(f'Vetor: {vetorN}')
    print(f'Média do vetor: {m:.2f}')
    print(f'Desvio Padrão: {dp ** (1 / 2):.5f}')

