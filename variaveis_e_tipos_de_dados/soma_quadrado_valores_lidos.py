"""
Programa que pede do usuário digitar três valores do tipo inteiro e soma os
seus quadrados.
"""
try:
    numeros = []
    for c in range(1, 4):
        num = int(input(f"Insira o {c}º valor: "))
        numeros.append(num)
    total = (numeros[0]**2) + (numeros[1]**2) + (numeros[2]**2)
    print(f"Total da soma quadrática de: {numeros[0]}, {numeros[1]} e {numeros[2]} é igual a {total}")
except (ValueError, KeyboardInterrupt) as exc:
    print("Insira somente valores inteiros!")
    print(f"Oops! Ocorreu um erro: {exc}")
