n = 3
i = 0
m = 0
while i < 10:
    mul = n * i
    if mul % n == 0:
        m = m + 1
        print(f'O {m}º valor {mul} é múltiplo de {n}')
        if m == 5:
            print(f'Esses são os {m} múltiplos de {n}')
            break
    i = i + 1
