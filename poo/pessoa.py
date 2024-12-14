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
        print(f'O sistema tem {len(cls.usuarios)} cadastrado(s)')

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
        """
        :return: retorna os dados do usuário que foi cadastrado na classe Pessoa
        """
        Pessoa.cadastro()  # Acessa o método estático e imprime uma mensagem de boas-vinda!
        return f'Nome: {self.__nome}\nData de Nascimento: {self.__nascimento}\nE-mail: {self.__email}'

    def idade(self):
        try:
            idade_atual = date.today().year - datetime.strptime(self.__nascimento, '%d/%m/%Y').year
            return f'{self.__nome} tem {idade_atual} anos'
        except ValueError as exc:
            return f"Erro: {exc}. Verifique o formato da data em {self.__nascimento}"


while True:

    nome_user = str(input('Insira seu nome: '))
    email_user = input('E-mail: ')
    nascimento_user = input('Data de nascimento (Exemplo: dia/mês/ano): ')

    usuario = Pessoa(nome_user, nascimento_user, email_user)
    consulta = input("Quer consultar seus dados? [Sim/Não]: ")

    if consulta == "Sim":  # Checa dados
        print(usuario.dados())
        print(usuario.idade())

    print('---------------------------------------------------------')
    continuar = input('Quer cadastrar mais? [Sim/Não]: ')
    if continuar in ['Não', 'nao', 'não', 'n', 'NÃO']:
        break


# Para consultar usuários cadastrados no sistema
Pessoa.usuario()

