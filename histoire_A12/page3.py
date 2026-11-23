
def page3(game_state: dict) -> int:
    print("")
    
    res : int = -2
    
    print("Tu trouves une armure") # TODO
    print("1- Tu l'équipes   2- Tu la laisses et tu continues ton chemin")

    choix : str = input("> ")
    
    if choix == "1":
        print("Tu équipes l'armure")
        print("DEF :", game_state["defense"], "->", game_state["defense"] + 2)
        game_state["defense"] = game_state["defense"] + 2
        res = 6
    elif choix == 2:
        print("Tu n'équipes pas l'armure et tu passes à la prochaine pièce")
        res = 6
    else:
        print("Choix invalide!")
        res = 3

    return res
    