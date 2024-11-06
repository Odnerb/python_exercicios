print('   SEQUÊNCIA FIBONACCI   ')
print('=========================')
n = int(input('Diga um número: '))
sf, fa, f = 0, 0, 0
while sf <= n:
    if fa <= 1:
        if sf == 0:
            print(fa)
        fa = fa + 1
    if fa == 1 and f == 1:
        print(f)
        sf = f + fa
        print(sf)
    elif sf == 0:
        sf = fa + f
        fa = f
        f = sf
        print(sf)
    elif sf != 0:
        sf = fa + f
        fa = f
        f = sf
        print(sf)


