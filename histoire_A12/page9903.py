from OUTILS.combat import combat
def page9903(game_state: dict) -> int:
    res : int = -2

    combat_gagne: bool = combat(game_state, {"nom":"Monstre", "pv":25, "defense":1, "attaque":4, "mult attaque puissante" : 3, "chance attaque puissante": .2})

    if combat_gagne:
        res = 9904
    else:
        res = -1

    return res
