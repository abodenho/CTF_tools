# Whois

https://www.kali.org/tools/whois/

## Description

Permet de récupéré les informations du serveur  (/auprès de serveur whois / *top level domain* [.com,.be,...])

# Nslookup 

https://www.ibm.com/docs/en/aix/7.2?topic=n-nslookup-command

## Description 

Permet de récupéré les informations du seveur auprès du serveur DNS 

## Commande 

1) *nslookpup -query=**#QUERY** **#ADRESS***

Où :

- **#QUERY** : est un type de demande (*ANY* si on veux toute les informations )

- **#ADRESS** : adresses ip cible 

2) *nslookpup -type=any -query=AXFR **#ADRESS***

(commande de zone de transfer)

Où :

- **#ADRESS** : adresses ip cible 

# Dig 

https://www.ibm.com/docs/en/aix/7.1?topic=d-dig-command

## Description 

Permet de récupéré les informations du seveur auprès du serveur DNS 

## Command 

*dig **#QUERY** **#ADRESS***

Où :

- **#QUERY** : est un type de demande (*any* si on veux toute les informations )

- **#ADRESS** : adresses ip cible 

## NOTE 

La différence entre *nslookup* et *dig* est que dig est plus fexible et facile à utilisé que nslookup mais plus restrictive

# Tiney

https://tineye.com/

## Description 

Permet de retrouver la source d'une image 

# file finder

https://file.org/

## Description 

Trouve la source de l'extension d'un fichier 

# Way back machinge 

https://archive.org/

## Description

Permet de voir les historiques des pages webs

# Way back URL

https://github.com/tomnomnom/waybackurls

## Description

Récupère l'url passé d'un site

# The haverester

https://github.com/laramies/theHarvester

## Description

Collecte tous les informations possible d'un site

# Virustotal

https://www.virustotal.com/gui/home/upload

## Description 

Vérifie fichier, URL, autre pour des éléments cachées

