
class Agenda:

    contatos = []

    @classmethod
    def armazenar_contato(cls, contato):
        Agenda.contatos.extend([contato])

    @classmethod
    def remove_contato(cls, numero):
        for indice, celular in enumerate(cls.contatos):
            if celular.get('Numero') == numero:  # Compara o número com cada um dos elementos do range da lista contatos
                del cls.contatos[indice]  # Remove número
                return f'O número {numero} foi removido.'

    @classmethod
    def buscar_contato(cls, nome):
        for indice, celular in enumerate(cls.contatos):
            if celular.get('Nome') == nome:
                return f'O contato {nome} está na posição {indice+1} da agenda.'

    @classmethod
    def imprimir_contato(cls, indice):
        return cls.contatos[indice - 1]

    @staticmethod
    def imprimir_agenda():
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


