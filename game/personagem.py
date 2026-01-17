import random

#estrutura do personagem
class Personagem:
    def __init__(self,nome,forca,agilidade,resistencia):
        #atributos
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.resistencia = resistencia

        self.vida = self.forca + self.resistencia
    #checagem se personagem esta vivo
    def vivo(self):
        return self.vida > 0
    #rolar 1d6
    def rolar_d6(self):
        return random.randint(1,6)

