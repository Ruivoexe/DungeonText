from game.inimigos import gerar_inimigo, gerar_boss_salao
from game.combate import combate


def cena_prisao(jogador):
    print('\n+++ CELA DA PRISÃO +++')
    print('Você acorda em uma cela fria, a porta está aberta\n')
    print('1- Sair pela porta')
    print('2- Vasculhar')

    escolha = input("Escolha: ")

    if escolha == '1':
        return cena_corredor(jogador)
    elif escolha == '2':
        print("Você encontra marcas antigas nas paredes... alguém esteve aqui.")
        return cena_prisao(jogador)
    else:
        print("Inválido")
        return cena_prisao(jogador)


def cena_corredor(jogador):
    print('\n+++ CORREDOR DA MASMORRA +++')
    print("Um corredor longo e silencioso se estende à sua frente.\n")
    print('1- Ir ao fim do corredor')
    print('2- Subir escadaria')
    print('3- Vasculhar')

    escolha = input("Escolha: ")

    if escolha == '1':
        inimigo = gerar_inimigo()
        resultado = combate(jogador, inimigo)

        if resultado == 'derrota':
            print("GAME OVER")
            return None

        return cena_corredor(jogador)

    elif escolha == '2':
        return cena_patio(jogador)

    elif escolha == '3':
        print("Parece abandonado a muito tempo")
        return cena_corredor(jogador)

    else:
        print("Erro")
        return cena_corredor(jogador)


def cena_patio(jogador):
    print('\n+++ PÁTIO DA FORTALEZA +++')
    print("Um grande pátio se abre diante de você.\n")
    print('1- Ir ao salão principal')
    print('2- Ir à capela')
    print('3- Ir ao portão principal')
    print('4- Voltar')
    print('5- Vasculhar')

    escolha = input("Escolha: ")

    if escolha == '1':
        inimigo = gerar_inimigo()
        if combate(jogador, inimigo) == 'derrota':
            print("GAME OVER")
            return None
        return cena_salaop(jogador)

    elif escolha == '2':
        inimigo = gerar_inimigo()
        if combate(jogador, inimigo) == 'derrota':
            print("GAME OVER")
            return None
        return cena_capela(jogador)

    elif escolha == '3':
        inimigo = gerar_inimigo()
        if combate(jogador, inimigo) == 'derrota':
            print("GAME OVER")
            return None
        return cena_portaop(jogador)

    elif escolha == '4':
        return cena_corredor(jogador)

    elif escolha == '5':
        print("Existem sinais de uma batalha antiga")
        return cena_patio(jogador)

    else:
        print("Erro")
        return cena_patio(jogador)


def cena_salaop(jogador):
    print('\n+++ SALÃO PRINCIPAL +++')
    print("Um grande salão em ruínas.\n")
    print('1- Ir ao trono')
    print('2- Voltar')
    print('3- Vasculhar')

    escolha = input("Escolha: ")

    if escolha == '1':
        if 'chave' in jogador.inventario:
            print("O guardião já foi derrotado.")
            return cena_salaop(jogador)

        print("A Armadura Vazia do Capitão se levanta!")
        inimigo = gerar_boss_salao()

        resultado = combate(jogador, inimigo)

        if resultado == 'derrota':
            print("GAME OVER")
            return None

        print("Você derrotou o Capitão!")

        if inimigo.tem_chave:
            print("Você encontrou a CHAVE DO PORTÃO!")
            jogador.inventario.append("chave")

        return cena_salaop(jogador)

    elif escolha == '2':
        return cena_patio(jogador)

    elif escolha == '3':
        print("Algo estranho aqui.")
        return cena_salaop(jogador)

    else:
        print("Erro")
        return cena_salaop(jogador)

def cena_capela(jogador):
    print('\n+++ CAPELA +++')
    print("Uma capela antiga, tomada pelo silêncio.\n")

    # Fantasma já usado → só voltar
    if jogador.fantasma_usado:
        print("O altar está silencioso. O espírito já partiu.")
        print("1- Voltar")
        input("Escolha: ")
        return cena_patio(jogador)

    print('1- Falar com o fantasma')
    print('2- Voltar')
    print('3- Vasculhar')

    escolha = input("Escolha: ")

    if escolha == '1':
        print("\nO fantasma sussurra palavras antigas...")
        print("Escolha um atributo para receber +1:")
        print("1- Força | 2- Agilidade | 3- Resistência")

        att = input("Escolha: ")

        if att == '1':
            jogador.forca += 1
            print("Sua Força aumentou!")

        elif att == '2':
            jogador.agilidade += 1
            print("Sua Agilidade aumentou!")

        elif att == '3':
            jogador.resistencia += 1
            jogador.recalcular_vida_maxima()
            print("Sua Resistência aumentou! Vida máxima ampliada.")

        else:
            print("Escolha inválida.")
            return cena_capela(jogador)

        jogador.fantasma_usado = True
        print("\nO fantasma desaparece em paz.")
        input("Pressione ENTER para continuar...")
        return cena_patio(jogador)

    elif escolha == '2':
        return cena_patio(jogador)

    elif escolha == '3':
        print("O altar está coberto de poeira.")
        return cena_capela(jogador)

    else:
        print("Erro")
        return cena_capela(jogador)



def cena_portaop(jogador):
    print('\n+++ PORTÃO PRINCIPAL +++')
    print("Um portão maciço bloqueia a saída.\n")
    print('1- Abrir portão')
    print('2- Voltar')
    print('3- Vasculhar')

    escolha = input("Escolha: ")

    if escolha == '1':
        if "chave" in jogador.inventario:
            print("Você abre o portão.")
            print("VOCÊ ESCAPOU DA MASMORRA!")
            print("FIM DA FASE 1")
            return None
        else:
            print("O portão está trancado.")
            return cena_portaop(jogador)

    elif escolha == '2':
        return cena_patio(jogador)

    elif escolha == '3':
        print("Marcas profundas de batalhas antigas.")
        return cena_portaop(jogador)

    else:
        print("Erro")
        return cena_portaop(jogador)
