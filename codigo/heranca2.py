## FORA DA LISTA ##
class Gamer:
    def __init__(self):
        self.__nome = ""
        self.__gamertag = 0

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

    def get_gamertag(self):
        return self.__gamertag
    def set_gamertag(self, gamertag):
        self.__gamertag = gamertag


class Streamer(Gamer):
    def __init__(self):
        Gamer.__init__(self)
        self.__plataforma = ""
        self.__numero_seguidores = 0

    def get_plataforma(self):
        return self.__plataforma
    def set_plataforma(self, plataforma):
        self.__plataforma = plataforma
    def get_numero_seguidores(self):
        return self.__numero_seguidores
    def set_numero_seguidores(self, numero_seguidores):
        self.__numero_seguidores = numero_seguidores


class Jogador(Gamer):
    def __init__(self):
        Gamer.__init__(self)
        self.__media = 0.0

    def calcular_media(self, pontuacao1, pontuacao2):
        self.__media = (pontuacao1 + pontuacao2) / 2
        return self.__media

    def get_media(self):
        return self.__media

    def set_media(self, media):
        self.__media = media

class JogadorCasual(Jogador):
    def __init__(self):
        Jogador.__init__(self)

    def aprovacao(self):
        if self.get_media() >= 6:
            return True
        else:
            return False
    def exibir_dados(self):
        return f"Nome: {self.get_nome()}, Gamertag: {self.get_gamertag()}, Promoção: {self.aprovacao()}"
class JogadorPro(Jogador):
    def __init__(self):
        Jogador.__init__(self)

    def aprovacao(self):
        if self.get_media() >= 8:
            return True
        else:
            return False

    def exibir_dados(self):
        return f"Nome: {self.get_nome()}, Gamertag: {self.get_gamertag()}, Promoção: {self.aprovacao()}"