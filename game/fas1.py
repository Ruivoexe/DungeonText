from inimigos import gerar_inimigo
from game.combate import combate

def cena_prisao(jogador):
    print('\n+++ CELA DA PRISÃO +++')
    print('voce acorda em uma cela fria, a porta esta aberta\n')
    print('1- Sair pela porta')
    print('2- Vasculhar')

    escolha = input("Escolha:")

    if escolha == '1':
        return cena_corredor(jogador)
    elif escolha == '2':
        print("Você encontra marcas antigas nas paredes... alguém esteve aqui.")
        return cena_prisao(jogador)
    else:
        print("invalido")
        return cena_prisao(jogador)

def cena_corredor(jogador):
    print('\n+++ CORREDOR DA MASMORRA +++')
    print("Um corredor longo e silencioso se estende à sua frente.\n")
    print('1- Ir ao fim do corredor')
    print('2- Subir escadaria')
    print('3- vasculhar')

    escolha = input("escolha: ")

    if escolha == '1':
        print("\nVocê caminha até o fim do corredor...")
        input("Pressione ENTER para continuar...")

        inimigo = gerar_inimigo()

        resultado = combate(jogador, inimigo)

        if resultado == 'derrota':
            print("game over")
            return None

        print("Continua após combate")
        return cena_corredor(jogador)

    elif escolha =='2':
        print("escadaria bloqueada")
        return cena_corredor(jogador)

    elif escolha == '3':
        print("nada")
        return cena_corredor(jogador)
    else:
        print("erro")
        return cena_corredor(jogador)

