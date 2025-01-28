"""
Programa que checa se o número informado é impar ou par
"""
try:
    num = int(input(f"Número: "))
    print(f"{f'O número {num} é par!' if num % 2 == 0 else f'O número {num} é impar!'}")
except (ValueError, KeyboardInterrupt) as exc:
    print("Insira somente valores inteiros!")
    print(f"Oops! Ocorreu um erro: {exc}")