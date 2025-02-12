print('==================================')
print('=      MAIOR E MENOR ALUNO       =')
print('==================================')

alunos: dict = {}
posicaoMa: int = 0
posicaoMe: int = 0

for c in range(0, 5):
    a = int(input(f'Número aluno: '))
    alt = float(input(f'Altura: '))
    aluno = {a: alt}
    alunos.update(aluno)

for c, v in alunos.items():
    if v == max(alunos.values()):
        posicaoMa = c
    elif v == min(alunos.values()):
        posicaoMe = c


if __name__ == "__main__":
    print('=============================================================================')
    print(f'Alunos: {alunos}')
    print(f'Maior aluno posição {posicaoMa}: {max(alunos.values())}m')
    print(f'Menor aluno posição {posicaoMe}: {min(alunos.values())}m')
