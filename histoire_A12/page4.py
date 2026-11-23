def page4(game_state:dict)->int:
    res : int = -2

    print("")

    print("Devant toi 3 porte")
    print("Choisis ta porte")
    print("1- Force . 2- Dexterite . 3- Intelligence")

    choix: str = input("> ")

    if choix == "1":
        res = 9 
    elif choix == "2":
        res = 10
    elif choix == "3":
        res = 11
    else:
        print("Choix Invalide!")
        res = 4

    return res