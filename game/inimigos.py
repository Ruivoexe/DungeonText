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

BOSS_SALAOP={
    "nome": "Armadura vazia do Capitão",
    "forca": 7,
    "agilidade": 7,
    "resistencia": 6,
    "drop": (120, 180),  # XP alto
    "chave": True
}


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

def gerar_boss_salao():
    dados = BOSS_SALAOP

    boss = Personagem(
        nome=dados["nome"],
        forca=dados["forca"],
        agilidade=dados["agilidade"],
        resistencia=dados["resistencia"]
    )

    boss.drop_min, boss.drop_max = dados["drop"]
    boss.tem_chave = dados.get("chave", False)

    return boss
