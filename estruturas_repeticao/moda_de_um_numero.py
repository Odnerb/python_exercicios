q = int(input('Quantos números serão lidos? '))
maior = 0
moda = 0
n = int(input('Diga um número: '))
for c in range(1, q):
    if n >= maior:
        maior = n
        if n == maior:
            moda += 1
        elif n != maior:
            maior = 0
    n = int(input('Diga um outro número: '))
