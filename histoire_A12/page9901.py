from OUTILS.divers import afficher_page_backrooms
def page9901(game_state: dict) -> int:
    res : int = -2

    print("")

    pages_adjacentes : dict = {"N": 9902, "S": 9903}

    afficher_page_backrooms(pages_adjacentes)

    choix: str = input("> ").upper()

    if choix in pages_adjacentes:
        res = pages_adjacentes[choix]
    else:
        print("Choix invalide")
        res = 9901

    return res