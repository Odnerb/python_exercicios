"""
Faça uma função que receba como parâmetro o valor de um ângulo em graus e
calcule o valor do seno desse ângulo usando sua respectiva série de Taylor:

x - (x^3/3!)/(x^5/5!)
1
"""


def taylor(angulo):
    x = angulo * 3.141593/180
    sen, seno = [x], 0

    for n in range(1, 5+1):
        expoente = 2 * n + 1
        fatorial, valor = 1, n + 2
        for f in range(1, expoente+1):
            fatorial *= f
        x = ((-1) ** n) * (x ** expoente) / fatorial
        sen.append(x)

    for i, valor in enumerate(sen):
        seno += valor

    return f"O seno do ângulo {angulo}° é de {seno:.2f}"


try:
    numero = float(input("O valor do ângulo em radianos: "))
    print(taylor(numero))

except (SyntaxError, ValueError, TypeError, StopIteration, OverflowError) as erro:
    print(f"Um erro foi encontrado: {erro}")
