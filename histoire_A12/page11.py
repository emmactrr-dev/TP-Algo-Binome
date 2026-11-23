from OUTILS.divers import wordle

## Porte de l'Intelligence

def page11(game_state: dict) -> int:
    res : int = -2

    print("")

    gagne : bool = wordle()

    if gagne:
        res = 12
    else:
        res = -1

    return res