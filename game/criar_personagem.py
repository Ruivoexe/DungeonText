from game import personagem
from personagem import Personagem
from classes import CLASSES

def criar_personagem(classe):
    print("\nCriação de personagem\n")
    nome = input("Nome: \n")
    atributos = CLASSES[classe].copy()

    print("\nVocê pode adicionar +1 em UM atributo:")
    print("1 - Força")
    print("2 - Agilidade")
    print("3 - Resistência")

    while True:
        escolha = input('> ')
        if escolha == '1':
            atributos['forca']+=1
            break
        elif escolha == '2':
            atributos['agilidade']+=1
            break
        elif escolha == '3':
            atributos['resistencia']+=1
            break
        else:
            print('erro')

    personagem = Personagem(
        nome = nome,
        forca=atributos["forca"],
        agilidade=atributos["agilidade"],
        resistencia=atributos["resistencia"]
    )

    return personagem