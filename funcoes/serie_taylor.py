"""
Faça uma função que receba como parâmetro o valor de um ângulo em graus e
calcule o valor do seno desse ângulo usando sua respectiva série de Taylor:

x - (x^3/3!)/(x^5/5!)
1
"""


def menu():
    print("---------------------------------")
    print(" Selecione a opção para calcular")
    print("---------------------------------")
    print("[1] - Seno")
    print("[2] - Cosseno")
    print("[3] - Seno Hiperbólico")
    print("[4] - Cosseno hiperbólico")
    print("[5] - Sair")
    print("---------------------------------")


def taylor(angulo, op):
    # Convertendo o ângulo para radianos
    x = angulo * 3.141593 / 180
    seno, cosseno = 0, 0

    if op == 1:
        for n in range(6):
            expoente = 2 * n + 1
            fatorial = 1
            for f in range(1, expoente+1):
                fatorial *= f
            termo = ((-1) ** n) * (x ** expoente) / fatorial
            seno += termo
        return f"O seno do ângulo {angulo}° é de {seno:.3f} graus"

    elif op == 2:
        for n in range(6):
            expoente = 2 * n
            fatorial = 1
            for f in range(1, expoente+1):
                fatorial *= f
            termo = ((-1) ** n) * (x ** expoente) / fatorial
            cosseno += termo
        return f"O cosseno do ângulo {angulo}° é de {cosseno:.3f} graus"

    elif op == 3:
        seno_hiperbolico = 0
        for n in range(6):
            expoente = 2 * n + 1
            fatorial = 1
            for f in range(1, expoente + 1):
                fatorial *= f
            termo = (x ** expoente) / fatorial
            seno_hiperbolico += termo

        return f"O seno hiperbólico do ângulo {angulo}° é de {seno_hiperbolico:.3f} graus"

    elif op == 4:
        coss_hiperbolico = 0
        for n in range(6):
            expoente = 2 * n
            fatorial = 1
            for f in range(1, expoente + 1):
                fatorial *= f
            termo = (x ** expoente) / fatorial
            coss_hiperbolico += termo

        return f"O cosseno hiperbólico do ângulo {angulo}° é de {coss_hiperbolico:.4f} graus"


try:
    menu()

    opcao = int(input("Opção: "))
    numero = float(input("O valor do ângulo em radianos: "))
    print(taylor(numero, opcao))

except (SyntaxError, ValueError, TypeError, StopIteration, OverflowError) as erro:
    print(f"Um erro foi encontrado: {erro}")
