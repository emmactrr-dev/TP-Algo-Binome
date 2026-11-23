def page7(game_state : dict) -> int:
    res : int = -2

    print("")

    intelligence : int = game_state["competences"]["INTELLIGENCE"]

    if intelligence == 3:
        print("Tu trouves un passage secret dans le mur, y entres-tu [Y/N]")
        choix : str = input("> ").upper()

        if choix == "Y":
            res = 8
        else:
            print("Tu trouves une dague")
            print("+ DAGUE")
            game_state["inventaire"].append("dague")
            game_state["piece 2 cherchée"] = True

            res = 2

    else:
        print("Tu trouves une dague")
        print("+ DAGUE")
        game_state["inventaire"].append("dague")
        game_state["piece 2 cherchée"] = True

        res = 2

    return res