from game.inimigos import gerar_inimigo
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
            #checar jogador.vivo() v ou f
            return None

        print("Continua após combate")
        return cena_corredor(jogador)

    elif escolha =='2':
        return cena_patio(jogador)

    elif escolha == '3':
        print("nada")
        return cena_corredor(jogador)

    elif escolha == '123':
        print("Não é um easter egg")
        #easter egg
    else:
        print("erro")
        return cena_corredor(jogador)




def cena_patio(jogador):
    print('\n+++ PÁTIO DA FORTALEZA +++')
    print("Um grande pátio se abre diante de você.\n")
    print('1- Ir ao salão principal')
    print('2- Ir a capela')
    print('3- Ir ao portão principal')
    print('4- voltar')
    print('5- Vasculhar')

    escolha = input("escolha: ")

    if escolha =='1':
        input("Pressione ENTER para continuar...")
        inimigo = gerar_inimigo()
        resultado = combate(jogador, inimigo)

        if resultado == 'derrota':
            print("game over")
            # checar jogador.vivo() v ou f
            return None
        else:
            return cena_salaop(jogador)

    elif escolha == '2':
        input("Pressione ENTER para continuar...")
        inimigo = gerar_inimigo()
        resultado = combate(jogador, inimigo)

        if resultado == 'derrota':
            print("game over")
            # checar jogador.vivo() v ou f
            return None
        else:
            return cena_capela(jogador)

    elif escolha == '3':
        input("Pressione ENTER para continuar...")
        inimigo = gerar_inimigo()
        resultado = combate(jogador, inimigo)

        if resultado == 'derrota':
            print("game over")
            # checar jogador.vivo() v ou f
            return None
        else:
            return cena_portaop(jogador)

    elif escolha == '4':
        return cena_corredor(jogador)

    elif escolha == '5':
        print("patio vazio")
        return cena_patio(jogador)

    else:
        print("erro")
        return cena_patio(jogador)

def cena_salaop(jogador):
    print('\n+++ SALÃO PRINCIPAL +++')
    print("Um grande salão vazio em ruinas.\n")
    print('1- Ir ao trono')
    print('2- voltar')
    print('3- Vasculhar')

    escolha = input("escolha: ")

    if escolha == '1':
        #boss com a chave para o portão principal
        #ainda n foi criado boss para a area, inimigo forte
        #print("Boss")
        input("Pressione ENTER para continuar...")
        inimigo = gerar_inimigo()
        resultado = combate(jogador, inimigo)

        if resultado == 'derrota':
            print("game over")
            # checar jogador.vivo() v ou f
            return None
        else:
            #recebe chave para abrir portão
            return cena_salaop(jogador)



    elif escolha == '2':
        return cena_patio(jogador)

    elif escolha == '3':
        print("uma armadura vazia no trono")
        return cena_salaop(jogador)

    else:
        print("erro")
        return cena_salaop(jogador)

def cena_capela(jogador):
    print('\n+++ CAPELA +++')
    print("Uma capela antiga, com um altar.\n")
    print('1- Falar com fantasma')
    print('2- voltar')
    print('3- Vasculhar')

    escolha = input("escolha: ")
    if escolha == '1':
        print("Voce é recebido pelo fantasma")
        return cena_capela(jogador)
        #jogador recebe +1 em um atributo de sua escolha
        #nao implementado

    elif escolha == '2':
        return cena_patio(jogador)

    elif escolha == '3':
        print("um fantasma solitario caminha pela capela")
        return cena_capela(jogador)

    else:
        print("erro")
        return cena_salaop(jogador)

def cena_portaop(jogador):
    print('\n+++ PORTÃO PRINCIPAL +++')
    print("Um robusto protão sobrevivente de muitas guerras.\n")
    print('1- Abrir portão')
    print('2- voltar')
    print('3- Vasculhar')

    escolha = input("escolha: ")
    if escolha == '1':
        print("o portão está trancado, necessita chave!")

        return cena_portaop(jogador)
        #precisa da chave que esta com boss na cena_salaop
        #abrir portão fim da fase 1

    elif escolha == '2':
        return cena_patio(jogador)

    elif escolha == '3':
        print("um portão grande")
        return cena_portaop(jogador)

    else:
        print("erro")
        return cena_portaop(jogador)