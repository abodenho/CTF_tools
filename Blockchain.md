# Cast 

https://book.getfoundry.sh/cast/

## Description

Permet de communiquer avec des blochain etherium RTC 

## Command 

cast send --rpc-url http://$IP:$PORT/rpc --private-key $PRIVATE_KEY $TARGET_ADDRESS $FONCTION $VALUES_FONCTION

Où : 

1) IP : une adresse ip 
2) PORT: un port de connection
3) PRIVATE_KEY : key de la session 
4) TARGET_ADDRESS : adresse ciblé
5) FONCTION : fonction à appeler ( string => " ")
6) VALUES_FONCTION : ensemble des arguments pour utilisé la fonction