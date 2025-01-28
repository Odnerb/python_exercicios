"""
Programa que pede do usuário digitar três valores do tipo inteiro e os soma
"""
try:
    numeros = []
    for c in range(1, 4):
        num = int(input(f"Insira o {c}º valor: "))
        numeros.append(num)
    print(f"Total da soma de {numeros[0]}, {numeros[1]} e {numeros[2]} é igual a {sum(numeros)}")
except (ValueError, KeyboardInterrupt) as exc:
    print("Insira somente valores inteiros!")
    print(f"Oops! Ocorreu um erro: {exc}")
