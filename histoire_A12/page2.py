

from OUTILS.divers import prendre_degats
def page2(game_state: dict) -> int:
    res : int = -2

    print("")


    print("Devant toi se trouve un ravin rempli de serpents")
    print("Que fais-tu?")
    
    print("1- Tu te bats comme un.e vaillant.e guerrier/ère . 2- Tu sautes au dessus du ravin . 3- Tu cherches la pièce pour t'aider")
    
    choix : str = input("> ")

    force : int = game_state["competences"]["FORCE"]

    if choix == "1":
        if force == 3 or (force == 2 and "dague" in game_state["inventaire"]):
            print("Tu les maraves.")
            res = 4
        elif force == 2 or (force == 1 and "dague" in game_state["inventaire"]):
            print("Tu les bats, mais tu te fais mordre, tu prends 3 dégâts") # Sale fragile
            prendre_degats(game_state, 3)
            res = 4
        elif force == 1:
            print("Tu meurs de leurs morsures") # Débile
            res = -1
        
    elif choix == "2":
        dexterite :int = game_state["competences"]["DEXTERITE"]
        if force == 3:
            print("Tu sautes tellement haut que tu te retrouves dans la pièce au dessus")
            res = 3
        elif dexterite == 3:
            print("Tu sautes au-dessus")
            res = 4
        elif dexterite == 2:
            print("Tu réussis à sauter au dessus, mais tu galères et tu te fais mordre")
            prendre_degats(game_state, 3)
            res = 4
        elif dexterite == 1:
            print("Tu trébuches et tu tombes dans un autre trou.")
            res = 5

    elif choix == "3":

        if game_state["piece 2 cherchée"]:
            print("Tu as déjà cherché cette pièce, tu ne trouves rien d'autre")
            res = 2
            
        else:
            res = 7

            
            

    else:
        print("Choix invalide!")
        return 2

    return res

