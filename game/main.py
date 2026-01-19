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

#primeiro teste de combate! SUCESSO
jogador = Personagem("pala", 5, 4, 6)
inimigo = Personagem("Monstro", 3, 3, 3)
resultado = combate(jogador, inimigo)
print("\nResultado do combate:", resultado)

#teste robusto de combate
# cria jogador fixo
jogador = Personagem(
    nome="soldado",
    forca=6,
    agilidade=6,
    resistencia=6
)

# gera inimigo aleatório
inimigo = gerar_inimigo()

print("=== JOGADOR ===")
print("Vida:", jogador.vida)
print("Força:", jogador.forca)
print("Agilidade:", jogador.agilidade)
print("Resistência:", jogador.resistencia)
print()

print("=== INIMIGO ===")
print("Nome:", inimigo.nome)
print("Vida:", inimigo.vida)
print("Força:", inimigo.forca)
print("Agilidade:", inimigo.agilidade)
print("Resistência:", inimigo.resistencia)
print()

# inicia combate
resultado = combate(jogador, inimigo)

print("\nResultado do combate:", resultado)

#teste de sistema de cenas e progressão de fases/ teste 1
from personagem import Personagem
from fase1_cenas import cena_prisao

# Criar jogador de teste
jogador = Personagem(nome="Herói", forca=6, agilidade=6, resistencia=6)

print("=== INÍCIO DA FASE 1 ===")

# Loop de execução das cenas
cena_atual = cena_prisao

while cena_atual and jogador.vivo():
    cena_atual = cena_atual(jogador)

print("\n=== FIM DA FASE 1 ===")
if not jogador.vivo():
    print("Seu herói caiu na masmorra.")
else:
    print("Você completou a fase 1!")


'''

from criar_personagem import criar_personagem
from fase1_cenas import cena_prisao
from classes import CLASSES

def escolher_classe():
    print("\nEscolha sua classe:")
    classes = list(CLASSES.keys())

    for i, nome in enumerate(classes, 1):
        print(f"{i} - {nome}")

    while True:
        escolha = input("> ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(classes):
            return classes[int(escolha) - 1]
        print("Escolha inválida")

def main():
    print("=== DUNGEON TEXT ===")

    classe = escolher_classe()
    jogador = criar_personagem(classe)

    cena_atual = cena_prisao

    while cena_atual and jogador.vivo():
        cena_atual = cena_atual(jogador)

    print("\n=== FIM DO JOGO ===")
    if not jogador.vivo():
        print("Seu herói morreu.")
    else:
        print("Fim da demo.")

if __name__ == "__main__":
    main()






