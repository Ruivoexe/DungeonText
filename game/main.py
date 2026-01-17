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
'''
from personagem import Personagem
from classes import CLASSES
from escolha_classes import escolher_classe

