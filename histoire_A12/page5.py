def page5(game_state: dict) -> int: ## BOSS DE FIN
    res : int = -2

    print("")


    if "épée" in game_state["inventaire"] or "arc" in game_state["inventaire"] or "baguette" in game_state["inventaire"]:
        # t'as l'arme tu peux gagner
        print("///") # TODO
    else:
        # t'es une merde
        print("Tu tombes dans une pièce lugubre et froide, tu ne vois rien à causes de la pénombre. Quand soudainement..")
        print("Une torche s'allume, et tu vois un vampire devant toi, confus.")
        print("'T'es pas censé déjà être là.'")
        #####

        res = -1

    return res

