import random
from personagem import Personagem

INIMIGOS = [
    {
        "nome": "Rato",
        "forca": 4,
        "agilidade": 4,
        "resistencia": 4,
        "drop": (20, 50)
    },
    {
        "nome": "Esqueleto",
        "forca": 5,
        "agilidade": 5,
        "resistencia": 5,
        "drop": (50, 70)
    },
    {
        "nome": "Armadura Vazia",
        "forca": 6,
        "agilidade": 6,
        "resistencia": 5,
        "drop": (70, 100)
    }
]

def gerar_inimigo():
    dados = random.choice(INIMIGOS)

    inimigo = Personagem(
        nome=dados["nome"],
        forca=dados["forca"],
        agilidade=dados["agilidade"],
        resistencia=dados["resistencia"]
    )

    inimigo.drop_min, inimigo.drop_max = dados["drop"]
    return inimigo
