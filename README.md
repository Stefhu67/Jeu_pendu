# Le jeu du pendu

Ce script propose une manière de réaliser un jeu du pendu à partir d'un mot extrait d'un fichier *.txt*.
Ce fichier peut soit :
- Être fourni par l'utilisateur au nom de *'mots_pendu.txt'*
- Ou lire un fichier de base 'mots.txt'

Attention de bien respecter le nom *'mots_pendu.txt'*.

## Packages et modules

Ce script fait appelle aux modules ```random``` et ```string``` déjà implémentés à ```Python 3```. 
Il ne nécessite donc aucune installation de package supplémentaire.

## Contenu et format du fichier .txt

Afin de lire correctement ce fichier, les lettres doivent être écrites en minuscules et 
chaque mot doivent être séparé par un saut à la ligne. 
Les mots peuvent prendre en compte les accents de la langue française comme : **'àâèéêëôîïûùüç'**.
Il est important que ce format soit respecté.\
Voici un exemple de fichier *.txt* accepté :
```
maçonnerie
captivité
démolition
guitare
avion
médecine
```

## Fonctions du script

Le fichier *jeu_pendu_sh.py* comporte le script du jeu du pendu. 
Il est organisé sous forme de fonction afin de résoudre les différentes tâches.

- La fonction ```lire_ficher_txt()``` permet de lire le fichier *.txt* et de générer une liste de mots pour le pendu.

- La fonction ```retirer_saut_de_ligne()``` retire les ```\n``` de chaque mot de la liste générée.

- La fonction ```retirer_doublon()``` retire les éventuels doublons dans la liste.

- La fonction ```modifier_caracteres_speciaux()``` modifie les caractères spéciaux **'àâèéêëôîïûùüç'** d'un mot en 
caractère normaux **aaeeeeoiiuuuc**.

- La fonction ```creer_liste_sans_caracteres_speciaux()``` appelle ```modifier_caracteres_speciaux()``` pour générer 
une liste de mots sans caractères spéciaux.

- La fonction ```choisir_item_aleatoire()``` permet de choisir un item aléatoire parmi une liste de mots ou un mot.
Dans le cas d'une liste de mots, l'item aléatoire sera un mot. Pour un mot, l'item sera une lettre.

- La fonction ```trouver_index_correspondants()``` fournit une liste des index correspondants à une lettre dans un mot.

- La fonction ```changer_lettre()``` permet de modifier une lettre d'un mot en fournissant une liste des index où se 
trouve la lettre.

- La fonction ```generer_enigme_pendu()``` génère un mot à trou à partir d'un sélectionné parmi une liste par 
```choisir_item_aleatoire()```. 
Cette fonction est utilisée à nouveau afin de générer une lettre aléatoire dans le mot. 
Celle-ci est positionnée à l'aide de ```trouver_index_correspondants()``` et ```changer_lettre()```.

- La fonction ```jouer_au_pendu()``` lance le jeu du pendu avec un mot à trou, sa solution et le nombre de chances fixé 
à 6. 
Tant que le nombre de chances n'est pas épuisé, l'utilisateur peut saisir une lettre afin de compléter le mot 
à trou. 
Si la lettre saisie figure dans la solution, le script complète le mot à trou avec ```trouver_index_correspondants()``` 
et ```changer_lettre()``` jusqu'à obtenir la solution complète. 
Sinon, l'utilisateur épuise une chance. 
S'il reste seulement une chance à l'utilisateur, la fonction lui fournira une lettre indice qui n'a pas encore testé 
et qui ne figure pas dans la solution. 
Au décompte du nombre de chances, l'utilisateur aura perdu.

## Déroulement du script

Lorsque l'utilisateur lance le script *jeu_pendu_sh.py*, l'interface lui demande s'il a fourni un fichier 
*mots_pendu.txt*.
Dans le cas contraire, le script prendra par défaut le fichier *mots.txt*.
Il exécute ```lire_ficher_txt()``` à partir du fichier *.txt*
Les sauts à la ligne ```\n```, les doublons ainsi que les caractères spéciaux sont retirés à l'aide de 
```retirer_saut_de_ligne()```, ```retirer_doublon()```, ```modifier_caracteres_speciaux()``` et 
```creer_liste_sans_caracteres_speciaux()```.
Il va ensuite prendre un mot aléatoire parmi la liste avec ```choisir_item_aleatoire()``` comme solution puis
créer un mot à trou avec ```generer_enigme_pendu()```.
Le jeu se lance avec ```jouer_au_pendu()```.
Il est possible de relancer le jeu à la fin de la partie avec un nouveau mot selon les désirs de l'utilisateur.