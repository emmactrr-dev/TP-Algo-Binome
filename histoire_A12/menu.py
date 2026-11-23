liste_competences : list = ["FORCE", "INTELLIGENCE", "DEXTERITE"]

def menu() -> dict:
    game_state : dict = {}

    print("Bonjour chère camarade.")
    print("Quel est ton nom?")
    nom : str = input("> ")
    
    
    print("Tu as trois compétences: Force, Intelligence et Dextérité.")
    print("Tu dois choisir une compétence HAUTE, MOYENNE et BASSE.")

    competences : dict = {}

    print("")

    # COMPETENCE HAUTE

    reponse_acceptee : bool = False
    indice_haute : int = choix_competence("HAUTE", competences)

    competence_haute : str = liste_competences[indice_haute]
    competences[competence_haute] = 3 

    print("")

    # COMPETENCE MOYENNE

    reponse_acceptee = False
    indice_moyenne : int = choix_competence("MOYENNE", competences)

    competence_moyenne : str = liste_competences[indice_moyenne]
    competences[competence_moyenne] = 2 

    print("")

    # COMPETENCE BASSE

    reponse_acceptee = False
    indice_bas : int = choix_competence("BASSE", competences)

    competence_basse : str = liste_competences[indice_bas]
    competences[competence_basse] = 1

    # ON CREE LE GAME STATE

    game_state = {
        "nom" : nom, 
        "pv" : 10,
        "defense" : competences["DEXTERITE"],
        "attaque" : 2 * competences["FORCE"],
        "competences" : competences,
        "inventaire" : [],

        "piece 2 cherchée" : False
    }

    return game_state

def choix_competence(niveau_competence : str, competences : dict) -> int:
    res : int = -1
    print(competences)
    reponse_acceptee : bool = False
    while not reponse_acceptee:
        print("Quelle est ta compétence", niveau_competence)
        print("0 - FORCE . 1 - INTELLIGENCE . 2 - DEXTERITE")
        res = int(input("> "))

        if res in [0,1,2] and liste_competences[res] not in competences:
            reponse_acceptee = True
        else:
            print("Réponse Invalide!")
            print("")

    return res
    