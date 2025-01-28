"""
Programa que verifica se um número é positivo ou negativo:
- Se positivo -> calcula a raiz quadrada do número;
- Se nagativo -> Imprime mensagem dizendo que o número é inválido;
"""
try:
    num = int(input(f"Número: "))
    print(f"{num ** 2 if num > 0 else 'Insira um número positivo e que seja maior que 0!'}")
except (ValueError, KeyboardInterrupt) as exc:
    print("Insira somente valores inteiros!")
    print(f"Oops! Ocorreu um erro: {exc}")
