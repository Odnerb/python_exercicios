from datetime import datetime
from datetime import date


class Pessoa:

    usuarios = []

    @classmethod
    def usuario(cls):
        """
        O método de classe armazena todos os usuários cadastrados no sistema
        Seguido de um loop for para visualização dos dados das Pessoas cadastradas.
        """
        print(f'O sistema tem {len(cls.usuarios)} cadastrados')

        for usuario in cls.usuarios:
            print(usuario)

    @staticmethod
    def cadastro():
        """
        Procedimento de boas vindas!
        """
        print('Usuário cadastrado com sucesso')
        print('------------------------------')

    def __init__(self, nome, nascimento, email):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__email = email
        self.__usuarios = Pessoa.usuarios.extend([{'Nome': nome, 'Data de nascimento': nascimento, 'E-mail': email}])

    def dados(self):
        Pessoa.cadastro()
        return f'Nome: {self.__nome}\nData de Nascimento: {self.__nascimento}\nE-mail: {self.__email}'

    def idade(self):
        idade_atual = date.today().year - datetime.strptime(self.__nascimento, '%d/%m/%Y').year
        return f'{self.__nome} tem {idade_atual} anos'


while True:
    nome_user = input('Insira seu nome: ')
    nascimento_user = input('Data de nascimento (Exemplo: dia/mês/ano): ')
    email_user = input('E-mail: ')

    usuario = Pessoa(nome_user, nascimento_user, email_user)

    print('---------------------------------------------------------')
    continuar = input('Quer cadastrar mais? [Sim/Não]: ')
    if continuar in ['Não', 'nao', 'não', 'n', 'NÃO']:
        break

# Para consultar usuários cadastrados no sistema
Pessoa.usuario()

