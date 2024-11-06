# Algoritmo que verifica se cada número é igual ao armazenado na lista.
# O programa não aceitará valores repetidos!

nums, cont, repetido, r = [], 1, 0, 0
while len(nums) <= 9:
    if r >= 10:
        print('FIM DE EXECUÇÃO DO PROGRAMA!')
        print('Usuário só repete valores...')
        break
    n = int(input(f'Diga o {cont}º número: '))
    nums.append(n)
    for c, v in enumerate(nums):
        if n == v:
            repetido = repetido + 1
            if n == v and repetido > 1:
                nums.remove(n)
                r = r + 1
                while n == v:
                    n = int(input(f'Diga outro número na posição {cont}º: '))
                    if n != v:
                        nums.append(n)
                    elif n == v:
                        print('Vamos tentar novamente...')
                        r = r + 1
                        if r >= 10:
                            break
    repetido = 0
    cont = cont + 1
print('=========================================================')
print(f'Lista de números: {nums}')
