from OUTILS.divers import prendre_degats

def page1(game_state: dict) -> int:
    res : int = -2

    print("")

    print("Bonjour", game_state["nom"], "tu te réveilles dans un donjon.")
    print(" //// ") # TODO : ECRIRE LE TEXTE

    print("Une porte est devant toi, que fais-tu?")

    if game_state["competences"]["INTELLIGENCE"] == 3:
        print("1- Essayer de défoncer la porte . 2- Essayer de crocheter la porte. 3- Essayer d'ouvrir la porte")

    else: ### PAS ASSEZ INTELLIGENT 
        print("1- Essayer de défoncer la porte . 2- Essayer de crocheter la porte.")

    choix : str = input("> ")
    

    if choix == "1":
        print("tu tombes elle est déjà ouverte sale con")
        prendre_degats(game_state, 1)
        res = 2
    elif choix == "2":
        # elle est déjà ouverte
        res = 2
    elif choix == "3" and game_state["competences"]["INTELLIGENCE"] == 3:
        # TODO TEXTE?
        res = 2
    elif choix == "BACKROOMS": # Cheat codes
        game_state["inventaire"].append("dague")
        game_state["attaque"] += 2
        res = 9901
    else:
        print("Choix invalide")
        res = 1

    return res