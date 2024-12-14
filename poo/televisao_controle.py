class Televisao:
    canal_tv = {
        4: "Globo",
        9: "Bande",
        11: "Record TV",
        13: "SBT",
        17: "RedeTV!",
        19: "Rede Vida",
        25: "TV Cultura",
        33: "TV Aparecida",
        52: "Canção Nova",
        531: "TV Brasil",
    }

    canal_atual = 4
    volume_atual = 20

    def __init__(self, volume=volume_atual, canal=canal_atual):
        """
         Por padrão, toda vez que a TV é ligada, ela inicia de onde parou
        :param volume: aumenta/diminui o volume
        :param canal: escolhe canal
        """
        self.volume = volume
        self.canal = canal
        self.status = False
        Televisao.volume_atual = self.volume
        Televisao.canal_atual = self.canal

    def status_televisao(self):
        """
        Método com Procedimento que verificar se a Televisao
        está ligada ou desligada. self.status irá receber a instância da classe ControleRemoto.
        Ao acionar o objeto "controle" a instância irá acionar o objeto da classe Televisao.

        Exemplo: tvlg.status_televisao() dentro de controle.botao_power(), que está sendo chamado como
        self.tvlg.status_televisao()  -> controle.tvlg.status_televisao().
        """
        if self.status:
            self.status = False
            print(f"Televisão desligada...")
        else:
            self.status = True
            print(f"Televisão ligada.")

    def status_volume(self, botao):
        """
        Método que verifica status do volume, o usuário tem a total liberdade de poder aumentar ou
        diminuir o volume de acordo com a quantidade de cliques quiser. Quando chega em ambas as extremidades
        de volume, imprime informações sobre a impossibilidade de novas alterações, pois atingiu o limite.
        :param botao: irá receber + para aumentar ou - para diminuir volume.
        """
        if (self.volume > 0) and (self.volume < 100):
            if botao == '+':
                self.volume += 1
                print(f"\U0001F509 {self.volume * '|'} {self.volume}")
            elif botao == '-':
                self.volume -= 1
                if self.volume != 0:
                    print(f"\U0001F509 {self.volume * '|'} {self.volume}")
        elif self.volume == 0:
            print(f"\U0001F507 {self.volume * '|'} {self.volume} Mudo")

        elif self.volume == 100:
            print(f"\U0001F507 {self.volume * '|'} {self.volume} Limite máximo")

    def status_canal(self, canal):
        """
        Método que verifica canais, se o usuário inserir um canal que não esteja na lista abaixo,
        o programa irá setar na tela que o canal está fora do ar. Caso o usuário digite um canal que
        esteja no ar, será acessado o atributo da classe Televisao e verificado dentro do dicionário
        qual emissora petercente da numeração. Cada valor (emissora) está com a chave do seu respectivo
        canal.
        :param canal:
        """
        if canal in [4, 9, 11, 13, 17, 19, 25, 33, 52, 531]:
            print(f"{Televisao.canal_tv.get(canal)} {canal} - NO AR\n")
        else:
            print(f"Canal {canal} - FORA DO AR.")
        pass


class ControleRemoto:

    def __init__(self, tvlg):
        """
        :param tvlg: recebe a Instância da classe Televisao
        """
        self.tvlg = tvlg

    def botao_power(self):
        """
        A instância acessa o método de instância da classe Televisao
        """
        self.tvlg.status_televisao()

    def botao_volume(self, botao):
        """
        :param botao: verifica se o usuário está apertando + ou -, ambos acessam o método de instância
        status_volume, que está presente na classe Televisao.
        """
        if botao == '+':
            self.tvlg.status_volume(botao)
        elif botao == '-':
            self.tvlg.status_volume(botao)

    def botao_canal(self, botao):
        self.tvlg.status_canal(botao)


tvlg = Televisao()
controle = ControleRemoto(tvlg)


def interface_controle():
    print("-----------------------------")
    print("     SELECIONE A OPÇÃO       ")
    print("-----------------------------")
    print("[on/off] - Ligar/Desligar TV ")
    print("[  +  ] - Aumentar volume    ")
    print("[  -  ] - Diminuir volume    ")
    print("[canal] - Escolher canal     ")
    print("-----------------------------")


def canais():
    print("-----------------------------")
    print("4 Globo                      ")
    print("9 Band                       ")
    print("11 Record TV                 ")
    print("13 SBT                       ")
    print("17 RedeTV!                   ")
    print("19 Rede Vida                 ")
    print("25 TV Cultura                ")
    print("33 TV Aparecida              ")
    print("52 Canção Nova               ")
    print("531 TV Brasil                ")
    print("-----------------------------")


decisao = input("Ligar TV? [Sim/Não]: ")

if decisao in "Sim":

    interface_controle()
    opcao = input("Selecionar opção: ")

    if opcao == "on":
        controle.botao_power()
        canais()
        canal = int(input("Canal: "))

        while opcao:

            print("===================================")
            controle.botao_canal(canal)
            print("===================================")

            trocar = input("Trocar de canal? [Sim/Não]")
            if trocar == "Sim":
                canais()
                canal = int(input("Canal: "))

            else:
                interface_controle()
                opcao = input("Selecionar opção: ")
                if opcao == "canal":
                    canais()
                    canal = int(input("Canal: "))

                elif opcao == "+":
                    botao = int(input("Apertar o botão quantas vezes: "))
                    for c in range(botao):
                        controle.botao_volume(opcao)

                elif opcao == "-":
                    botao = int(input("Apertar o botão quantas vezes: "))
                    for c in range(botao):
                        controle.botao_volume(opcao)

                elif opcao == "off":
                    controle.botao_power()
                    break

    elif opcao in ["+", "-", "canal"]:
        print("Ligue a TV primeiramente...")

    else:
        print("Nada feito...")
        print("Ligue a TV")
