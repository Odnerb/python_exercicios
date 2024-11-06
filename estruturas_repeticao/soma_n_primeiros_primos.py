num = int(input('Diga um número: '))
sum = 0
if num > 0:
    for n in range(1, num+1):
        if n % 2 == 0:
            print(end='')
        elif (n % 1 == 0) and (n % n == 0):
            sum = sum + n
    print(f'A soma dos primeiros números de {num} primos é {sum}')
