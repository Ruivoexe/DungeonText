from classes import CLASSES

def escolher_classe():
    print("Escolha sua classe: ")
    nomes_classes = list(CLASSES.keys())

    for i, nome in enumerate(nomes_classes,start=1):
        atributo = CLASSES[nome]
        print(f"{i} - {nome.capitalize()} "
              f"(Força: {atributo['forca']}, "
              f"Agilidade: {atributo['agilidade']}, "
              f"Resistência: {atributo['resistencia']})")
    while True:
        escolha = input('Escolha sua classe: ')
        if escolha.isdigit():
            indice = int(escolha) -1
            if 0<=indice<len(nomes_classes):
                return nomes_classes[indice]

        print('erro')

