print('   SOMANDO SEQUÊNCIA FIBONACCI   ')
print('=================================')
n = int(input('Diga um número: '))
sf, fa, f = 0, 0, 0
while sf <= n and sf <= 4_000_000:
    if fa <= 1:
        if fa % 2 == 0:
            if sf == 0:
                print(fa)
        fa = fa + 1
    elif sf == 0:
        if sf % 2 == 0 or sf == 0:
            sf = fa + f
            fa = f
            f = sf
            print(sf)
    elif sf != 0:
        if sf % 2 == 0:
            sf = fa + f
            fa = f
            f = sf
            print(sf)
