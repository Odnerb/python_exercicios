s, d = 0, 0
for i in range(1, 99, 2):
    d = d + 1
    for j in range(1, 51):
        if j == d:
            s = s + (i/j)
print(s)
