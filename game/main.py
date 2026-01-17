'''
Debugs:
#teste script personagem
p=Personagem('teste',5,4,4)
print(p.nome)
print('vida: ',p.vida)
print('vivo?',p.vivo())
print(p.rolar_d6())

#teste script classes
print('Classes disponiveis: ')
for nome,atributo in CLASSES.items():
    print(nome,atributo)

#teste de escolha de classe
classe = escolher_classe()
print('Classe: ',classe)

# testando sistema de criação de personagem
classe = escolher_classe()
jogador =  criar_personagem(classe)

print("\nPersonagem criado com sucesso!")
print("Nome:", jogador.nome)
print("Força:", jogador.forca)
print("Agilidade:", jogador.agilidade)
print("Resistência:", jogador.resistencia)
print("Vida:", jogador.vida)

#teste de geração de inimigos
inimigo = gerar_inimigos()

print("\nUm inimigo apareceu!")
print("Nome:", inimigo.nome)
print("Força:", inimigo.forca)
print("Agilidade:", inimigo.agilidade)
print("Resistência:", inimigo.resistencia)
print("Vida:", inimigo.vida)
print("Defesa:", inimigo.defesa)
print("Drop:", inimigo.drop, "moedas")

#teste de rolagem do jogador
heroi = Personagem("Teste", 4, 4, 4)

print("Acerto:", heroi.calcular_acerto())
print("Dano:", heroi.calcular_dano())
print("Defesa:", heroi.defesa())
print("Vida antes da cura:", heroi.vida)
print("Cura:", heroi.curar())
print("Vida após cura:", heroi.vida)

#teste de função defendendo()
jogador = Personagem("Heroi", 4, 4, 4)
jogador.vida = 5

jogador.defendendo()
print("Vida:", jogador.vida)
print("Defesa:", jogador.defesa())

#teste de função de fuga
jogador = Personagem("Herói", 4, 4, 4)
resultado = jogador.fugir()
print("Resultado da fuga:", resultado)


'''
from personagem import Personagem
from classes import CLASSES
from escolha_classes import escolher_classe
from criar_personagem import criar_personagem
from inimigos import gerar_inimigos
from personagem import Personagem




