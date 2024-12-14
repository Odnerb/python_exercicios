class Agenda:
    contatos = []  # Atributo de classe que armazena os contatos na lista

    @classmethod
    def armazenar_contato(cls, contato):
        """
        Método de classe para armazenamento de números telefônicos.
        :param contato: recebe um contato que irá ser armazenado no atributo de classe contatos
        Agenda.contatos.extend(): acessa a classe e atualiza a lista.
        """
        Agenda.contatos.extend([contato])

    @classmethod
    def remove_contato(cls, numero):
        """
        Método de classe que exclui número, remove_contato() é composto por um loop for
        que irá iterar sobre cada indice até encontrar o número que o usuário deseja remover
        e tirá-lo da lista. Isso ocorre porque dentro da lista contém uma outra coleção, do tipo dict.
        :param numero: recebe o número que irá ser removido da lista telefônica.
        """
        for indice, celular in enumerate(cls.contatos):
            if celular.get('Numero') == numero:  # Compara o número com cada um dos elementos do range da lista contatos
                del cls.contatos[indice]  # Remove número
                return f'O número {numero} foi removido.'

    @classmethod
    def buscar_contato(cls, nome):
        """
        Método de classe que verifica qual o número da pessoa com base no nome consultado pelo o usuário,
        retorna o indice da posição da pessoa, dentro da lista telefônica pesquisada.
        :param nome:
        :return: o nome do contato e o indice onde encontra-se na lista.
        """
        for indice, celular in enumerate(cls.contatos):
            if celular.get('Nome') == nome:
                return f'O contato {nome} está na posição {indice+1} da agenda.'  # Recebe +1, porque todo o loop for
                # não retorna o último elemento de um range. E também para referir-se a quantidade de usuários digitados
                # no sistema.

    @classmethod
    def imprimir_contato(cls, indice):
        """
        :param indice: caso o usuário busque o indice de determinado usuário e o encontre no método acima, neste método
        de classe, será mostrado somente o contato do usuário que ele deseja visualizar.
        :return: atributo de classe retorna os dados do contato buscado pelo indice.
        """
        return cls.contatos[indice - 1]

    @staticmethod
    def imprimir_agenda():
        """
        Procedimento que mostra todos os usuários armazenados na lista telefônica.
        """
        for celular in Agenda.contatos:
            print(celular)

    def __init__(self, nome, contato):
        self.__nome = nome
        self.__contato = contato


def menu():
    print('     LISTA TELEFÔNICA     ')
    print('--------------------------')
    print('[1] - Armazenar contato')
    print('[2] - Remover contato')
    print('[3] - Buscar contato')
    print('[4] - Imprimir agenda')
    print('[5] - Imprimir contato')
    print('Pressione outras teclas para Sair...\n')


while True:
    menu()
    nome_conta, numero, contato = '', '', {}
    opcao = int(input('Selecione o número da opção desejada: '))

    if opcao == 1:
        nome_conta = input('Nome: ')
        numero = input('Celular: ')
        celular = Agenda(nome_conta, numero)
        contato = {'Nome': nome_conta, 'Numero': numero}
        Agenda.armazenar_contato(contato)

    elif opcao == 2:
        if len(Agenda.contatos) != 0:
            numero = input('Remover número: ')
            print(Agenda.remove_contato(numero))

    elif opcao == 3:
        nome = input('Buscar nome: ')
        print(Agenda.buscar_contato(nome))

    elif opcao == 4:
        Agenda.imprimir_agenda()

    elif opcao == 5:
        indice = int(input('Indice do contato: '))
        print(Agenda.imprimir_contato(indice))

    else:
        break


