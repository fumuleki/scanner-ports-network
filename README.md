# scanner-ports-network
Cet script a pour but d'automatiser l'analyse des milliers de ports de notre serveurs, router et machines de reseau en une seconde.
En informatique, le scan de ports est une technique servant à rechercher les ports ouverts sur un serveur de réseau.
Cette technique est utilisée par les administrateurs des systèmes informatiques pour contrôler la sécurité des serveurs de leurs réseaux. La même technique est aussi utilisée par les pirates informatiques pour tenter de trouver des failles dans des systèmes informatiques.

Cet article vous montrera comment vous pouvez créer un petit programme d'automatiser l'analyse de port de notre reseau facile à utiliser écrit en Python. Il existe de nombreuses façons de faire cela avec Python, et je vais le faire en utilisant le module intégré Socket.

# Sockets

Le module socket en Python permet d'accéder à l'interface socket BSD. Il comprend la classe socket, pour gérer le canal de données réel, et des fonctions pour les tâches liées au réseau telles que la conversion du nom d'un serveur en une adresse et le formatage des données à envoyer sur le réseau.
Les prises source sont largement utilisées sur Internet, car elles sont à l'origine de tout type de communications réseau effectuées par votre ordinateur.
Les Sockets INET représentent au moins 99% des sockets utilisées. Le navigateur Web que vous utilisez ouvre un socket et se connecte au serveur Web.
Toute communication réseau passe par une socket.
# Le scan de ports c'est quoi ?

Un scan de port a pour objectif de m'indiquer quels sont les ports ouverts sur une machine. Un port ouvert est un port en état LISTEN s'il s'agit de TCP, ou simplement en écoute s'il s'agit d'UDP.

# Créer un script à l'aide des sockets Python

Comment créer un script d'analyse de port en Python.
Ce script d'analyse de port essaiera de se connecter sur chaque port que vous définissez pour un hôte particulier. La première chose que nous devons faire est d'importer la bibliothèque de sockets dont nous avons besoin.

# Ouvrez un éditeur de texte, copiez et collez le code ci-dessous.
# Enregistrez le fichier sous: «scanner_ports.py» et quittez l'éditeur
  
  #!/usr/bin/python3

  import socket

def scan(host, port):

# Nous avons également mis en place une gestion des erreurs pour détecter les erreurs

    try:
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.connect((host, port))
        
        s.settimeout(0.5)
        
    except socket.error:
    
        return False
        
    return True
    
# Ask for input

host = input('GIVE ME A HOST NAME : ')

# Utilisation de la fonction de plage pour spécifier les ports (ici, il analysera tous les ports entre 1 et 5000)


def check_port(host):

    for i in range(1, 5000):
    
        if scan(host, i):
        
            print('The port :',i,' at :', host,' is open')
            
        print('The port :',i,' at :', host,' is close')
        

check_port(host)

Pour la démonstration je l'ai enregistré sous le nom "scanner_ports.py" puis entré la commandre suivante dans le terminal de linux: python3 scanner_ports.py
Il suffit ensuite de suivre les instructions affichées pour l'utiliser. 
Le résultat retournes la liste des differents ports ouverts et fermés que le script a découvert.
    
