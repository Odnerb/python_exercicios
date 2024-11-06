f = 1
s = 1/2 # como o fatorial de 2 é ele mesmo, na soma já atribuo ele.
for i in range(2, 12, 1):
    for j in range(1, i):
        if f == 0:
            f = i * j
        elif f > 0:
            f = f * j
    print(f)
    c = 1
    if f % 2 == 0 and i <= 10:
        while c < i:
            if c == (i - c):
                df = c/f
                s = s + df
            c = c + 1
        f = 0
print(s)
