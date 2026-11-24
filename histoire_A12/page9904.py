from OUTILS.divers import est_numerique
from ast import ClassDef
from OUTILS.divers import prendre_degats
from time import sleep
def page9904(game_state: dict) -> int:
    res : int = -2

    print("Tu trouves un coffre en bois!")
    for i in range(7):
        sleep(0.5)
        print(". \n")
    print("Il est fermé.")

    print("Comment l'ouvres-tu?")
    if "dague" in game_state["inventaire"]:
        print("'DAGUE': Tu utilises la dague pour le crocheter.")
    if "torche" in game_state["inventaire"]:
        print("'TORCHE': Tu utilises la torche pour le brûler.") 

    print("1: T'essayes de casser la serrure avec ta force . 2: Tu essayes de trouver le digicode")
    choix : str = input("> ")


    if choix == "1":
        if game_state["competences"] == 3:
            print("Tu petes le coffre en un coup")
            ...
            res = 9907
        if game_state["competences"] == 2:
            print("Tu arrives a casser le coffre mais tu fais mal a la main")
            prendre_degats(game_state, 5, True)
        if game_state["competences"] == 1:
            print("Tu te DETRUIS le bras sur le bois")
            pv :int = prendre_degats(game_state, 15)
            if pv <= 0:
                res = -2
            else:
                res = 9907
    if choix == "2":
        print("Entre le code à 3 chiffres.")
        code_joueur : str = ""
        code_secret : str = "425"
        abandon : bool = False
        
        while code_joueur != code_secret and not abandon: 
            print("")
            print("Entre le code ou 'ABANDON' pour arrêter")
            code_joueur = input("> ").upper()
            if code_joueur == "ABANDON":
                abandon = True
            elif not est_numerique(code_joueur) or len(code_joueur) > 3:
                print("Choix Invalide! \n")
            else:
                if len(code_joueur) < 3:
                    code_joueur = "0" * (3-len(code_joueur))
                
                if code_joueur < code_secret:
                    print("Plus grand!")
                
                if code_joueur > code_secret:
                    print("Plus petit!")
        if abandon:
            res = 9904
        else:
            ### coffre ouvert
            res = 9909
        """verif if code trouve ou abandon"""
    else:
        print("Choix Invalide!")
        res = 9904

    return res