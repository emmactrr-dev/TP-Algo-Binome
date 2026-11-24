def page4(game_state:dict)->int:
    res : int = -2

    print("")

    print("Devant toi 3 porte")
    print("Choisis ta porte")
    print("1- Force . 2- Dexterite . 3- Intelligence . 4- Tu voles la torche")

    choix: str = input("> ")

    if choix == "1":
        res = 9 
    elif choix == "2":
        res = 10
    elif choix == "3":
        res = 11
    elif choix == "4" and "torche" not in game_state["inventaire"]:
        print("Tu prends la torche avec toi!")
        game_state["inventaire"].append("torche")
        res = 4
    else:
        print("Choix Invalide!")
        res = 4

    return res