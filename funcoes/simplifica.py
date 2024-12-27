def divisao(funcao):
    def fator(*args):
        """
        :param args: recebe as tuplas vindas da função decorada simplifica e são desempacotadas em outras variáveis
        internas da função.
        :return: retorna o resultador da divisão
        """
        fator_valores, valor_numerador, valor_denominador = funcao(*args)
        print(f'Simplificando a divisao de {valor_numerador}/{valor_denominador} por {fator_valores}')
        print(f'Temos os valores {int(valor_numerador/fator_valores)}/{int(valor_denominador/fator_valores)}')
        return f'Que é igual a {valor_numerador/valor_denominador}'
    return fator


@divisao
def simplifica(numerador, denominador):
    """
    :param numerador: recebe um valor para ser dividido pela totalidade de denominador, esse valor tem que ser menor de
    que denominador.
    :param denominador: representa a totalidade de uma fração.
    :return: para evitar um código muito complexo e extenso, o ideal é chamar o decorador @divisao, portanto aqui nesta
    função decorada, só serão retornados os valores do fator, numerador e denominador para serem desempacotados na outra
    que irá uitlizá-la para retornar uma melhor visualização dos dados fatorados e o resultado.
    """
    valores = []
    if numerador < denominador:
        for num in range(1, numerador):
            if numerador % num == 0 and denominador % num == 0:
                valores.append(num)
    else:
        print('O numerador tem que ser menor ou igual ao denominador.')
    fator = max(valores)
    return fator, numerador, denominador


print(simplifica(45, 55))

