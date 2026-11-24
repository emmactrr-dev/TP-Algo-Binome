from random import random
from random import choice

def prendre_degats(etat : dict, degats : int, afficher: bool = True) -> int:
    degats_pris : int = max(degats - etat["defense"], 0) # On évite les dégâts négatifs
    
    if afficher:
        print("PV:", etat["pv"], "->", etat["pv"] - degats_pris)

    etat["pv"] = etat["pv"] - degats_pris
    
    return degats_pris



liste_mot : list = ["CHIEN", "POMME", "ADIEU", "MERDE"]
def wordle() -> bool:
    gagne : bool = False

    mot_secret : str = choice(liste_mot)

    essais : int = 0

    while not gagne and essais < 6:
        mot_devine : str = input("> ").upper()

        if mot_devine in liste_mot:
            essais = essais + 1

            couleurs : str = correction_couleurs(mot_devine, mot_secret)
            afficher_mot(mot_devine, couleurs)

        if mot_devine == mot_secret:
            gagne = True

    if gagne:
        print("T'as trouvé le mot")
    else:
        print("Perdu")

    return gagne

def correction_couleurs(mot_devine: str, mot_secret: str) -> str:
    couleurs : list = ["R", "R", "R", "R", "R"]

    # VERT
    for i in range(5):
        if mot_devine[i] == mot_secret[i]:
            couleurs[i] = "V"
        
    # JAUNE
    for i in range(5):
        if couleurs[i] == "R": # Si elle est déjà verte, on ignore
            lettre : str = mot_devine[i]


            if lettre in mot_secret:
                lettres_deja_verifiees : list = indices_couleurs(couleurs, ["J", "V"])
                # on vérifie si on a déjà assez vu la lettre
                if compte_lettre(mot_devine, lettre, lettres_deja_verifiees) < compte_lettre(mot_secret, lettre, list(range(5))):
                    couleurs[i] = "J"

    return "".join(couleurs) # On transforme la liste en string 


def indices_couleurs(couleurs: list, couleurs_acceptees: list):
    indices : list = []
    for i in range(len(couleurs)):
        if couleurs[i] in couleurs_acceptees:
            indices.append(i)
    
    return indices
    
        
def compte_lettre(mot : str, lettre: str, indices : list) -> int:
    compte : int = 0
    
    for i in indices:
        if i < len(mot) and mot[i] == lettre:
            compte = compte + 1

    return compte


def afficher_mot(mot : str, couleurs : str) -> None:
    res : None = None

    codes_couleurs : dict = {"R" : "91m", "V": "92m", "J": "93m"}


    texte_a_afficher : str = ""

    for i in range(len(mot)):
        couleur : str = couleurs[i]

        texte_a_afficher = texte_a_afficher + "\033[" + codes_couleurs[couleur] + mot[i] + "\033[00m"

    print(texte_a_afficher)

    return res

mot_directions : dict = {"N" : "Nord", "S":"Sud", "E":"Est", "O":"Ouest"}
def afficher_page_backrooms(pieces_adjacentes: dict) -> None:
    res : None = None

    print("Tu vas où? Tes choix sont:")
    for direction in pieces_adjacentes:
        print(mot_directions[direction], "(" + direction + ")")

    return res


def choix_page(possibilites : tuple):
    res : int = -2

    r : float = random() ## r entre 0 et 1 aléatoire
    somme_probas : float = 0 
    for possibilite in possibilites:
        somme_probas = somme_probas + possibilite[1]
        if r <= somme_probas and res == -2: ## on évite de changer plusieurs fois la valeur
            res = possibilite[0]


    return res
    

def est_numerique(string : str) -> bool:
    res : bool = True
    for c in string:
        if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            res = False
    return res