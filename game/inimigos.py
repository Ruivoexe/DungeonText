import random
from personagem import Personagem

INIMIGOS = [
    {
        "nome": "Rato",
        "forca": 2,
        "agilidade": 2,
        "resistencia": 2,
        "vida": 4,
        "acerto_base": 2,
        "dano_base": 2,
        "defesa": 2 * 2,
        "drop": (20, 50)
    },
    {
        "nome": "Esqueleto",
        "forca": 3,
        "agilidade": 3,
        "resistencia": 3,
        "vida": 7,
        "acerto_base": 3,
        "dano_base": 3,
        "defesa": 3 * 2,
        "drop": (50, 70)
    },
    {
        "nome": "Armadura Vazia",
        "forca": 5,
        "agilidade": 4,
        "resistencia": 5,
        "vida": 10,
        "acerto_base": 5,
        "dano_base": 5,
        "defesa": 4 * 2,
        "drop": (70, 100)
    }
]

def gerar_inimigos():
    dados = random.choice(INIMIGOS)
    inimigo = Personagem(
        nome=dados["nome"],
        forca=dados["forca"],
        agilidade=dados["agilidade"],
        resistencia=dados["resistencia"],

    )

    inimigo.vida = dados["vida"]
    inimigo.acerto_base = dados["acerto_base"]
    inimigo.dano_base = dados["dano_base"]
    inimigo.defesa = dados["defesa"]
    inimigo.drop = random.randint(dados["drop"][0], dados["drop"][1])

    return inimigo
