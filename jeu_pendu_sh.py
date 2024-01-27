import random
import string


# Créer une liste de mot à partir d'un fichier .txt
def lire_ficher_txt(nom_fichier):
    # Lire le fichier txt
    with open(nom_fichier, 'r') as fichier:
        # Obtenir une liste de chacune des lignes du txt
        ligne_fichier = fichier.readlines()

    # Retourner la liste
    return ligne_fichier


# Retirer les sauts à la ligne '\n' à partir d'une liste de mots
def retirer_saut_de_ligne(liste_mots):
    # Initialiser une liste vide
    liste_mots_sans_saut = []

    # Pour chaque mot dans la liste
    for chaque_mot in liste_mots:
        # Retirer les '\n'
        nouveau_mot = chaque_mot.strip()

        # Ajouter le mot sans '\n' dans la nouvelle liste
        liste_mots_sans_saut.append(nouveau_mot)

    # Retourner la liste de mot sans les '\n'
    return liste_mots_sans_saut


# Retirer les doublons d'une liste
def retirer_doublon(liste):
    return list(dict.fromkeys(liste))


# Modifier les caractères spéciaux 'àâèéêëôîû' d'un mot
def modifier_caracteres_speciaux(mot, caracteres_speciaux='àâèéêëôîïûùüç', caracteres_normaux='aaeeeeoiiuuuc'):
    # Pour chaque lettre du mot
    for lettre in mot:

        # Si la lettre est parmi les caractères spéciaux
        if lettre in caracteres_speciaux:
            # Trouver sa position dans les caractères spéciaux
            index_correspondant = caracteres_speciaux.find(lettre)

            # Remplacer la lettre par un caractère normal
            mot = mot.replace(lettre, caracteres_normaux[index_correspondant])

    # Retourner le mot sans caractères spéciaux
    return mot


# Créer une nouvelle liste de mots sans caractères spéciaux à partir d'une liste
def creer_liste_sans_caracteres_speciaux(liste_mots):
    # Créer une nouvelle liste vide
    liste_mot_sans_caracteres_speciaux = []

    # Pour chaque mot dans la liste
    for chaque_mot in liste_mots:
        # Modifier les caractères spéciaux dans le mot
        nouveau_mot = modifier_caracteres_speciaux(chaque_mot)

        # Ajouter le nouveau mot dans la nouvelle liste
        liste_mot_sans_caracteres_speciaux.append(nouveau_mot)

    # Retourner une nouvelle liste de mots sans caractères spéciaux
    return liste_mot_sans_caracteres_speciaux


# Choisir un item aléatoire (mot ou lettre) d'une liste de mot ou d'un mot
def choisir_item_aleatoire(liste_mots_ou_mots):
    return random.choice(liste_mots_ou_mots)


# Trouver les index correspondants à une lettre dans un mot
def trouver_index_correspondants(mot, lettre):
    # Créer une liste vide pour collecter l'index dans le mot
    liste_index_occurrence = []

    # Initialisation de l'index
    index_correspondant = 0

    # Pour chaque lettre du mot donné
    for chaque_lettre in mot:

        # Si elle est égale à la lettre donnée
        if chaque_lettre == lettre:
            # Collecter l'index dans la liste
            liste_index_occurrence.append(index_correspondant)

        # Augmenter d'index
        index_correspondant += 1

    # Retourner une liste des index où la lettre donnée se positionne dans le mot
    return liste_index_occurrence


# Modifier une lettre d'un mot à partir de sa/ses positions
def changer_lettre(mot, lettre, liste_index):
    # Convertir le mot en liste de chaque lettre
    mot = list(mot)

    # Pour chaque position de la lettre, modifier l'élément de la liste correspondant
    for chaque_index in liste_index:
        mot[chaque_index] = lettre

    # Reconvertir la liste en mot
    mot = ''.join(mot)

    # Retourner le mot
    return mot


# Créer une énigme du jeu pendu à partir d'un mot
def generer_enigme_pendu(mot):
    # Initialiser un string vide pour l'énigme
    enigme_pendu = ''

    # Ajouter des '_' pour chaque lettre du mot
    for _ in mot:
        enigme_pendu += '_'

    # Choisir une lettre aléatoire dans le mot choisi
    lettre_aleatoire = choisir_item_aleatoire(mot)

    # Trouver les index correspondants à une lettre dans un mot
    liste_index_correspondant = trouver_index_correspondants(mot, lettre_aleatoire)

    # Retourner l'énigme avec une lettre aléatoire
    return changer_lettre(enigme_pendu, lettre_aleatoire, liste_index_correspondant)


# Jouer au pendu avec une énigme d'un mot et un nombre de chances
def jouer_au_pendu(enigme, mot, nombre_chance=6, chance=0):
    # Les choix possibles pour le mot
    reponses_possibles = string.ascii_lowercase

    print(f"Voici les choix possibles en minuscules: {reponses_possibles}")
    print("Voici l'énigme: ")

    # Tant qu'il y a suffisamment de chances, on relance la boucle
    while chance < nombre_chance:

        print(enigme)
        print(f'Chances restantes: {nombre_chance - chance}\n')

        lettre_saisie = input(str('Saisir une lettre puis appuyer sur "Entrer": '))

        # Si la lettre saisie est dans le mot
        if lettre_saisie in mot:

            # Si la lettre figure déjà dans l'énigme
            if lettre_saisie in enigme:

                print(f"La lettre entrée figure déjà dans l'énigme. Recommencez!")

            # Sinon ajouter la lettre saisie à l'énigme
            else:
                print(f'Vous avez trouvé la lettre "{lettre_saisie}". \n')

                # On retrouve la ou les positions de la lettre dans le mot puis on modifie l'énigme
                liste_lettre_saisie = trouver_index_correspondants(mot, lettre_saisie)
                enigme = changer_lettre(enigme, lettre_saisie, liste_lettre_saisie)

            # Si l'énigme égale au mot, dans ce cas le jeu est gagné
            if enigme == mot:
                print(f'Félicitation, vous avez gagné! Vous avez trouvé le mot: {mot}')
                break

        # Si la lettre saisie n'est pas dans le mot
        else:
            print(f'Faux!, la lettre "{lettre_saisie}" ne figure pas dans le mot. Réessayer!\n')

            # On perd une chance
            chance += 1

            # Si on a épuisé toutes ses chances, le jeu est perdu
            if chance == nombre_chance:
                print('Vous avez utilisé toutes vos chances, vous avez été pendu(e)!')
                print(f'La réponse était: {mot}.\n')
                break

            # Pour la dernière chance, on donne un indice
            if chance == nombre_chance - 1:
                print('Il te reste une dernière chance...')

                # On choisit une lettre dans les réponses possibles restantes
                indice = choisir_item_aleatoire(reponses_possibles)

                # Tant que la lettre choisie figure dans le mot, on en choisit une autre
                while indice in mot:
                    indice = choisir_item_aleatoire(reponses_possibles)

                print(f"Petit indice, la lettre '{indice}' n'est pas dans le mot!")

                # Retirer l'indice des réponses possibles
                reponses_possibles = reponses_possibles.replace(indice, '')

        # Retirer la lettre des réponses restantes
        reponses_possibles = reponses_possibles.replace(lettre_saisie, '')
        print(f"Les choix possibles restants sont: {reponses_possibles}.\n")


# Savoir si l'utilisateur a fourni un fichier .txt
print("Il est l'heure de jouer au pendu!\n")
print('Avez-vous fourni une fichier du nom "mots_pendu.txt"?')
condition_utilisateur = int(input('Si oui, taper "1" puis "Entrer". Sinon, taper "2" puis "Entrer": '))

if condition_utilisateur == 1:

    # Si l'utilisateur a répondu "oui", le script va lire 'mots_pendu.txt'
    fichier_txt = 'mots_pendu'

else:

    # Sinon le script lit par défaut 'mots.txt'
    fichier_txt = 'mots'

# Génération d'une liste de mots à partir du fichier txt sans doublon et sans caractères spéciaux
liste_mots_fichier_brut = lire_ficher_txt(fichier_txt + '.txt')
liste_mots_fichier = retirer_saut_de_ligne(liste_mots_fichier_brut)
liste_mots_fichier = retirer_doublon(liste_mots_fichier)
liste_mots_fichier = creer_liste_sans_caracteres_speciaux(liste_mots_fichier)

# Conversion de la liste de mots en tuple
liste_mots_fichier = tuple(liste_mots_fichier)


# Boucle pour jouer au jeu du pendu
lancer_le_jeu = 1

while lancer_le_jeu == 1:
    # Choisir un mot aléatoire dans la liste de mots
    mot_aleatoire = choisir_item_aleatoire(liste_mots_fichier)

    # Génération de l'énigme du pendu à partir du mot aléatoire
    mot_pendu = generer_enigme_pendu(mot_aleatoire)

    # Jouer au pendu avec l'énigme et le mot aléatoire
    jouer_au_pendu(mot_pendu, mot_aleatoire)

    # Relancer le jeu si l'utilisateur le souhaite
    lancer_le_jeu = int(input('Voulez-vous rejouer? Oui: Appuyer sur "1" puis "Entrer", sinon "2" puis "Enter": \n'))
