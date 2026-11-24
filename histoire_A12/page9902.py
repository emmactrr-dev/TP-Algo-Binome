from OUTILS.divers import choix_page
from OUTILS.divers import afficher_page_backrooms
def page9902(game_state: dict) -> int:
    res : int = -2

    print("")

    pages_adjacentes : dict = {"N": ((9906, 1)), "S": ((9901, 0.67), (9905, 0.33))}

    afficher_page_backrooms(pages_adjacentes)

    choix: str = input("> ").upper()

    if choix in pages_adjacentes:
        res = choix_page(pages_adjacentes[choix])
    else:
        print("Choix invalide")
        res = 9901

    return res