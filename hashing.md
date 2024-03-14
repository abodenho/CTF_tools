# Jhon the ripper

https://github.com/openwall/john

## Description

Ensemble de programme en python permetant de récupéré les hashs des mot de passe des zips, word, excel, ... sécurisé.

## Command

*python **#NOM_PROGRAMME** **#PATH***

Où : 

- **#NOM_PROGRAMME** : Est le programme python 
- **#PATH** : est le chemin vers le fichier à extraire le hash

# Hashid

https://github.com/psypanda/hashID

## Description

Permet de trouvé de quel algorithme un hashing provient 

## Commande

*hashid **#HASH***

où :

- **#HASH** : est le hash à revert pour connaitre sa provenance  

# Hash cat 

## Description

Recherche le texte à l'origine d'un hash 


## Commande

*hashcat -a **#MODE** -m **#FORMAT_HASH**  **#HASH** **#[INFORMATION_SUPPLEMENTAIRE_MODE]***


Où : 

- **#MODE** : est le type de recherche (word list, hybride, brute force, ... )
- **#FORMAT_HASH** : est de quel algorithme provient le hash 
- **#HASH** : le hash à craqué
- **#[INFORMATION_SUPPLEMENTAIRE_MODE]** : les information supplémentaire à donnée lié au **#MODE**

NB : les valeurs de **#MODE**,  **#FORMAT_HASH** et **#[INFORMATION_SUPPLEMENTAIRE_MODE]** sont donnée en faisant "hashcat -h"


## Outilles supplémentaire 

### Dictionnaire de mots à télécharger 

- https://github.com/danielmiessler/SecLists/tree/master/Passwords
- https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm 

### Créateur de dictionnaire 

#### Crunch 

https://www.kali.org/tools/crunch/

Génère des listes avec des règles particulière

### CUPP

https://github.com/Mebus/cupp

Génère une liste de mot selon le profil d'un victime

### Prince 

https://github.com/hashcat/princeprocessor

Génère une liste sur une liste déja existante