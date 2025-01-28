"""
Programa que recebe dois valores e verifica qual deles é o maior.
"""

try:
    a = int(input(f"Insira o 1º valor: "))
    b = int(input(f"Insira o 2º valor: "))
    if a > b:
        print(f"O número {a} é maior que o número {b}.")
    else:
        print(f"O número {b} é maior que o número {a}.")
except (ValueError, KeyboardInterrupt) as exc:
    print("Insira somente valores inteiros!")
    print(f"Oops! Ocorreu um erro: {exc}")
