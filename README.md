# Projet TipTop
Un petit projet créé avec 3 amis dans le cadre de nos cours de NSI (en utilisant Tkinter et les bases de donnés relationnelle)
## Comment utiliser TipTop ?
ouvrez le fichier "fett.py" (Front-End TipTop) et lancez-le.
###
Le reste est assez facile à comprendre, vous pouvez créer un compte et des posts, voir d'autres posts et changer votre biographie grâce à la fenetre tkinter.
###
Gardez cependant en tête que toutes les données sont sauvegardées sur le fichier "dbtt.db" (database tiptop) et qu'il est situé dans les dossiers locaux.
###
Pour pouvoir réellement avoir un réseau, il faut placer le fichier "dbtt.db" dans un fichier accessible par tout le monde, puis changer la fonction "initcur()" dans "bett.py" (back-end tiptop) (la ligne "conn = sqlite3.connect('votre chemin d'accés')")
###
Vous me voyez aussi désolé du manque de lisibilité du script.
