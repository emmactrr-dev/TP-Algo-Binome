## Porte de la Force

from OUTILS.combat import combat
def page9(game_state: dict) -> int:
    res : int = -2

    print("")

    combat_gagne : bool = combat(game_state, {"nom":"José", "pv":20, "defense":1, "attaque":4, "mult attaque puissante" : 2, "chance attaque puissante": .5})

    if combat_gagne:
        print("Bv")
        res = 12
    else:
        print("T'es mort, fallait faire des meilleurs choix gamin")
        res = -1


    return res