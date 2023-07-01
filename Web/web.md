# dotdotpwn

https://www.kali.org/tools/dotdotpwn/

## Description

Permet de faire un une attaque ***directory traversal*** par fuzzing 

# curl

https://github.com/curl/curl

## Description

Transfere de donnée avec la syntaxe url



# Netcat 

https://www.kali.org/tools/netcat/


## Decription

Ouvre une connection TCP / UDP avec un serveur 

# Wget 

https://linux.die.net/man/1/wget

## Description

Téléchargement de fichier de manière non interactive sur le web

# xfreerdp 

https://linux.die.net/man/1/xfreerdp

## Description 

Permet de se connecté à distance depuis linux à une machine windows (Remote destkop protocol (RDP))

## Command 

1) *xfreerdp /v:**#IP**  /u:**#LOGIN** /p:**#PASWWORD***

Où : 

- **#IP** : l'adresse de la cible
- **#LOGIN** : le login d'un comtpe de la machine
- **#PASWWORD** : le mot de passe du **#LOGIN**

2) *xfreerdp /v:**#IP**  /u:**#LOGIN** /p:**#PASWWORD** /drive:**#PATH_DRIVE_CURRENT_MACHIN***

Où : 

- **#IP** : l'adresse de la cible
- **#LOGIN** : le login d'un comtpe de la machine
- **#PASWWORD** : le mot de passe du **#LOGIN**
- **#PATH_DRIVE_CURRENT_MACHIN**: installe sur la machine cible un "drive réseau" vers la machine actuelle. (par exemple : "linux,/home" path vers home)

# rdesktop 

http://www.rdesktop.org/

## Description 

RDP depuis linux vers windows

## Command 

rdesktop **#IP** -u **#LOGIN**  -p **#PASWWORD** -r disk:linux=**#PATH_DRIVE_CURRENT_MACHIN**

Où : 

- **#IP** : l'adresse de la cible
- **#LOGIN** : le login d'un comtpe de la machine
- **#PASWWORD** : le mot de passe du **#LOGIN**
- **#PATH_DRIVE_CURRENT_MACHIN**: installe sur la machine cible un "drive réseau" vers la machine actuelle. (par exemple : "/home" path vers home)


# Crt

https://crt.sh/

## Description

Récupère le certificat SSL/TLS  

# Netcraft

https://sitereport.netcraft.com

## Description

Récupère les infromation d'un site de manière passive



# Whatweb

https://morningstarsecurity.com/research/whatweb

## Description

Outil permetant de faire le listing des technologie d'un site web 


# Wawfw00f

https://github.com/EnableSecurity/wafw00f

## Description

Détecte les firewall d'une application web


# AQUATONE

https://github.com/michenriksen/aquatone

## Description 

Permet d'analyser la surface du site web pour voir quel endroit on peu attaqué 

## Instalation

sudo apt install golang chromium-driver
go get github.com/michenriksen/aquatone
export PATH="$PATH":"$HOME/go/bin"


# ZoneTransfers

https://hackertarget.com/zone-transfer/

## Description

Outille permetant de voir les information qu'un DNS principale envoie au DNS secondaire

# Gobuster


## Description 

Recherceh de sous domaine par énumération (/ fuzzing) 

## Code 

*gobuster dns -q -r **#DNS** -d **#ADRESSE** -w **#WORDLIST** -p **#FILE_PATERN** -o output.TXT*

Où : 

- **#DNS** : DNS spécifique 
- **#ADRESSE** : nom de domaine cible 
- **#WORDLIST** : list de mot servant au fuzzing


## Supplément 

### File patern format

exemple de patern : 
- lert-api-shv-{GOBUSTER}-sin6
- atlas-pp-shv-{GOBUSTER}-sin6

avec **#WORDLIST** = " 1 2 3 5 6"

avec 

Donne les résultats 

- lert-api-shv-01-sin6.facebook.com 
- atlas-pp-shv-01-sin6.facebook.com
- atlas-pp-shv-02-sin6.facebook.com
- atlas-pp-shv-03-sin6.facebook.com
- lert-api-shv-03-sin6.facebook.com
- lert-api-shv-02-sin6.facebook.com
- lert-api-shv-04-sin6.facebook.com
- atlas-pp-shv-04-sin6.facebook.com

### Seclists

https://github.com/danielmiessler/SecLists

Liste permetant de faire le fuzzing


# Zed Attacj Proxy

https://www.zaproxy.org/

## Description

Outille permetant de faire du crawling (listage de tous les ressource lors de l'exploration)


# ffuf 

## Description 

(1) Permet de faire du fuzzing de virtual host (serveur contenant plusieurs domaine virtuel) on attaque l'ip avec le HOST header pour récupéré des sous domaine

(2) Premet de faire du fuzzing permetant de trouver les dossier caché 

## Commande

1) *ffuf -w **#WODLIST** -u **#IP** -H **#FUZZING_HEADER***


Où : 

- **#WODLIST** : chemin vers la liste de mot servant au fuzing
- **#IP** : addresse IP du serveur (par exemple http://192.168.10.10 ) 
- **#FUZZING_HEADER** : message dans le header servant au fuzzing (par exemple : "HOST: FUZZ.randomtarget.com" où FUZZ est remplacé par les mots de la **#WODLIST**)

2) *ffuf -recursion -recursion-depth 1 -u **#IP**  -w **#WODLIST***

Où : 

- **#WODLIST** : chemin vers la liste de mot servant au fuzing
- **#IP** : addresse IP du serveur ( par exemple : http://192.168.10.10/FUZZ où FUZZ est remplacé par les mots de la **#WODLIST** ) 
