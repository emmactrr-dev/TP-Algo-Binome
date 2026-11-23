"""
Fonctions annexes pour les combats.

Ces fonctions ne décident JAMAIS de la page suivante : elles retournent
une information (ici True / False) et c'est la page qui choisit la suite.

Pour les utiliser dans une page :
    from OUTILS.combat import combat_dragon
"""


from pickletools import read_unicodestring1
from OUTILS.divers import prendre_degats
from random import random

def combat(game_state: dict, monstre: dict) -> bool:
    """
    Combat générique entre le héros et un monstre.

    gameState : le dictionnaire du jeu (contient "pv" et "force" du héros)
    monstre   : un dictionnaire avec les clés "nom", "pv" et "force"

    Retourne True si le héros gagne, False s'il perd.
    Les points de vie du héros perdus pendant le combat sont retirés
    de gameState["vie"].
    """
    res: bool = False

    recharge_atk_puissante : int = 0

    while game_state["pv"] > 0 and monstre["pv"] > 0:
        print("PV", game_state["nom"], ":", game_state["pv"], "| PV", monstre["nom"], ":", monstre["pv"])

        mult_attaque_monstre : bool = 1
        if random() <= monstre["chance attaque puissante"]:
            print(monstre["nom"], "va te niquer ta race")
            attaque_puissante = monstre["mult attaque puissante"]


        print("1- Attaque puissante (Dispo dans ", recharge_atk_puissante," tours) . 2- Attaque normale . 3- Defense")
        choix : str = input("> ")


        if choix == "1" and recharge_atk_puissante == 0:
            print("Grosse attaque")
            print("Dégâts:", prendre_degats(monstre, int(1.5*game_state["attaque"]), False))
            recharge_atk_puissante = 2

            print("Le dragon t'attaque")
            print("Dégâts:", prendre_degats(game_state, monstre["attaque"]*mult_attaque_monstre, False))
        elif choix == "2":
            print("Tu attaques le dragon!")
            print("Dégâts:", prendre_degats(monstre, game_state["attaque"], False))
            
            print("Le dragon t'attaque")
            print("Dégâts:", prendre_degats(game_state, monstre["attaque"]*mult_attaque_monstre, False))
        elif choix == "3":
            print("Tu bloques le coup du dragon!")
        
            print("Le dragon t'attaque")
            print("Dégâts:", prendre_degats(game_state, monstre["attaque"]*mult_attaque_monstre - game_state["defense"], False))
            # On "double" la défense en l'enlevant 2 fois aux dégats du monstre
        else:
            print("Choix invalide!")
            recharge_atk_puissante = recharge_atk_puissante + 1 # éviter la recharge quand le choix est invalide

        recharge_atk_puissante = max(0, recharge_atk_puissante - 1)

        print("")


    res = game_state["pv"] > 0


    return res


def combat_dragon(gameState: dict) -> bool:
    """Combat contre un dragon. Retourne True si le héros gagne."""
    monstre: dict = {"nom": "dragon", "vie": 20, "force": 4}
    res: bool = combat(gameState, monstre)
    return res


def combat_orc(gameState: dict) -> bool:
    """Combat contre un orc. Retourne True si le héros gagne."""
    monstre: dict = {"nom": "orc", "vie": 8, "force": 2}
    res: bool = combat(gameState, monstre)
    return res
