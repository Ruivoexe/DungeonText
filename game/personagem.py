import random
from rolagem import rolar_1d6

#estrutura do personagem
class Personagem:
    def __init__(self,nome,forca,agilidade,resistencia):
        #atributos
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.resistencia = resistencia

        self.vida_maxima = self.forca + (self.resistencia*2)
        self.vida = self.vida_maxima

        self.lamentos = 0
        self.em_defesa = False

    #checagem se personagem esta vivo
    def vivo(self):
        return self.vida > 0

    #equação de atributos
    def calcular_acerto(self):
        return self.agilidade+rolar_1d6()

    def calcular_dano(self):
        return self.forca+rolar_1d6()

    def curar(self):
        cura = rolar_1d6()
        self.vida += cura

        if self.vida > self.vida_maxima:
            self.vida=self.vida_maxima

        return cura

    #habilidades/açoes
    def defesa(self):
        defesa_base = self.resistencia+self.forca
        #checagem do estado defendendo
        if self.em_defesa:
            print('Esta se defendendo!')
            return defesa_base*2
        return defesa_base

    def ataque(self,alvo):
        alvo.em_defesa = False
        teste_acerto = self.calcular_acerto()+rolar_1d6()
        defesa_alvo = alvo.defesa()

        print(f'{self.nome} ataca {alvo.nome}!')

        if teste_acerto > defesa_alvo:
            dano = self.calcular_dano()
            alvo.vida -= dano

            if alvo.vida<0:
                alvo.vida=0

            print(f"ataque acertou {alvo.nome} sofreu {dano}!")
            print('rolagem:',teste_acerto)
        else:
            print("errou")

    def defendendo(self):
        print("Assumiu posição defensiva!")
        self.em_defesa = True
        rolagem = rolar_1d6()
        print("Rolagem:", rolagem)

        if rolagem % 2==0:
            cura = self.curar()
            print("curou-se: ",cura)
        else:
            print("falha")

    def fugir(self):
        rolagem = rolar_1d6()
        print('tenta fugir: ',self.nome)
        print("rolagem: ",rolagem)

        if rolagem %2==0:
            print("fugiu!")
            return True
        else:
            print('falha')
            return False



