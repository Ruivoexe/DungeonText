import random


def combate(jogador, inimigo):
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Uma maldição cruza o seu caminho!', inimigo.nome)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')

    turno_jogador = random.choice([True, False])

    if turno_jogador:
        print('Jogador começa o combate\n')

    while jogador.vivo() and inimigo.vivo():

        if turno_jogador:
            print("\n+++ Seu Turno +++")
            print('Sua vida:', jogador.vida)
            print('Vida do inimigo:', inimigo.vida)

            print('\n1 - Atacar')
            print('2 - Defender')
            print('3 - Fugir')

            escolha = input('Escolha sua ação: ')

            if escolha == '1':
                jogador.ataque(inimigo)

            elif escolha == '2':
                jogador.defendendo()

            elif escolha == '3':
                if jogador.fugir():
                    print('Fuga com sucesso!')
                    return 'fuga'
                else:
                    print('Falhou na fuga!')

            else:
                print('Ação inválida!')

        else:
            print('\n+++ Turno do Inimigo +++')
            inimigo.ataque(jogador)

        turno_jogador = not turno_jogador

    # pós-combate
    if not jogador.vivo():
        print("Você morreu!")
        return 'derrota'

    print("Você venceu o combate!")

    # drop / recompensa (XP futuramente)
    if hasattr(inimigo, 'drop_min'):
        drop = random.randint(inimigo.drop_min, inimigo.drop_max)
        print(f"O inimigo deixou algo para trás ({drop})")

    return 'vitoria'
