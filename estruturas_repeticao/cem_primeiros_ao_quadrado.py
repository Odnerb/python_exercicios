s, sq = 0, 0
for c in range(1, 101):
    s = s + (c**2)
    sq = sq + c
    if c == 100:
        sq = sq**2
print(f'A soma dos 100 primeiros naturais é {s}')
print(f'O quadrado dos 100 primeiros naturais é {sq}')
print(f"""A diferença entre a soma dos 100 primeiros
números naturais e o quadrado da soma é {sq - s}""")
