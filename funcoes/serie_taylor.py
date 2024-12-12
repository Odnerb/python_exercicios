"""
Faça uma função que receba como parâmetro o valor de um ângulo em graus e
calcule o valor do seno desse ângulo usando sua respectiva série de Taylor:

x - (x^3/3!)/(x^5/5!)
1
"""


def taylor(angulo, cat):
    # Convertendo o ângulo para radianos
    x = angulo * 3.141593 / 180
    seno, cosseno = 0, 0

    if cat == 'sen':
        for n in range(6):  # 5 termos, de 0 a 5
            expoente = 2 * n + 1
            fatorial = 1
            for f in range(1, expoente + 1):
                fatorial *= f
            termo = ((-1) ** n) * (x ** expoente) / fatorial
            seno += termo
        return f"O seno do ângulo {angulo}° é de {seno:.4f}"

    elif cat == 'cos':
        for n in range(6):  # 5 termos, de 0 a 5
            expoente = 2 * n
            fatorial = 1
            for f in range(1, expoente + 1):
                fatorial *= f
            termo = ((-1) ** n) * (x ** expoente) / fatorial
            cosseno += termo
        return f"O cosseno do ângulo {angulo}° é de {cosseno:.4f}"


try:
    numero = float(input("O valor do ângulo em radianos: "))
    cateto = input("Cateto [sen|cos]: ")
    print(taylor(numero, cateto))

except (SyntaxError, ValueError, TypeError, StopIteration, OverflowError) as erro:
    print(f"Um erro foi encontrado: {erro}")
