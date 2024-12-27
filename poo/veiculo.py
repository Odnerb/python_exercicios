class Veiculo:

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self):
        raise NotImplementedError(f'Insira as informações de acordo com o tipo de veículo')

    @property
    def ver_marca(self):
        return self.__marca

    @property
    def ver_modelo(self):
        return self.__modelo

    @ver_marca.setter
    def ver_marca(self, nova_marca):
        self.__marca = nova_marca

    @ver_modelo.setter
    def ver_modelo(self, novo_modelo):
        self.__modelo = novo_modelo


class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas

    def __str__(self):
        print('Informações do veículo do tipo: Carro')
        print('-------------------------------------')
        return f'Marca: {self.ver_marca}\nModelo: {self.ver_modelo}\nNúmero de portas: {self.total_portas}'

    @property
    def total_portas(self):
        return self.__portas

    @total_portas.setter
    def total_portas(self, qnt):
        self.__portas = qnt


if __name__ == '__main__':
    fiat = Carro('Fiat', 'Uno', 4)
    print(fiat.ver_marca)
    print(fiat.ver_modelo)
    print(fiat.total_portas)
    print()
    print(fiat)
    print()
    fiat.total_portas = 6
    print(fiat.ver_marca)
    print(fiat.ver_modelo)
    print(fiat.total_portas)
    print()
    print(fiat)




