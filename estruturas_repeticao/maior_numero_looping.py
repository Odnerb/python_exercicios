n, maiorn = 0, 0
c = 1
while n >= 0:
    n = int(input(f'Diga o {c}º número: '))
    if n > maiorn:
        maiorn = n
    if n < 0:
        break
    c = c + 1
print(f'O maior número digitado foi: {maiorn}')
