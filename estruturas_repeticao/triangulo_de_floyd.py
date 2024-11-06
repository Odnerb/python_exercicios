print('   TRIÂNGULO DE FLOYD   ')
print('========================')
tf = 0
num = int(input('Insira a quantidade de linhas: '))
for c in range(1, num+1):
    for n in range(1, c+1):
        tf = tf + 1
        if n <= c:
            print(tf, end=' ')
    print()
