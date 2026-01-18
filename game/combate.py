import random

def combate(jogador,inimigo):
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Uma maldição cruza o seu caminho! ',inimigo.nome)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')

    #sorteio de iniciativa
    turno_jogador = random.choice([True,False])

    if turno_jogador:
        print('jogador começa o combate\n')


    #loop de combate
    while jogador.vivo() and inimigo.vivo():
        if turno_jogador:
            print("+++ Seu Turno +++")
            print('vida: ',jogador.vida)
            print('vida do inimigo:',inimigo.vida)

            print('\n1-atacar')
            print('2-defender')
            print('3-fugir')

            escolha = input('Escolha sua ação: ')
            if escolha == '1':
                jogador.ataque(inimigo)
            elif escolha == '2':
                jogador.defendendo()
            elif escolha == '3':
                if jogador.fugir():
                    print('fuga com sucesso!')
                    return 'fuga'

            else:
                print('invalido')


        else:
            print('turno do inimigo')
            inimigo.ataque(jogador)

        turno_jogador = not turno_jogador
    if not jogador.vivo():
        print("morto!")
        return('derrota')

    print('venceu')

    def dropar(inimigo):
        return random.randint(inimigo.drop_min, inimigo.drop_max)
        print(dropar(inimigo))
    return('venceu')


