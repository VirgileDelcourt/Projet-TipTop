#BASE DE DONNEES

import sqlite3
import random

def initcur(): #utilisé pour initier le curseur (cur) et la connection (conn)
    #la variable conn et cur sont globales
    global conn
    global cur
    conn = sqlite3.connect('dbTT') #Création d'une base de données
    cur = conn.cursor()

def commitcur(): #ferme le curseur et la connection
    conn.commit()
    cur.close()
    conn.close()
    

# creation des tables si elles n'existent pas
initcur()
cur.execute("CREATE TABLE IF NOT EXISTS USERS(id_user INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, password TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS POSTS(id_post INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, text TEXT, id_user INT, likes INT)")
cur.execute("CREATE TABLE IF NOT EXISTS COMMENTS(id_comment INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, text TEXT, id_user INT, id_post INT)")
cur.execute("CREATE TABLE IF NOT EXISTS LIKES(id_user INT, id_post INT)")
commitcur()

# creation d'un compte
def creation_compte(pseudo, mdp):
    if check_compte(pseudo):
        return False
    nv = (pseudo, mdp)
    initcur()
    cur.execute("INSERT INTO USERS(name, password) VALUES(?, ?)", nv)
    commitcur()
    return True


# check si un compte existe
def check_compte(pseudo, id_user = 0):
    initcur()
    if id_user == 0:
        cur.execute("SELECT name FROM USERS")
        conn.commit()
        check = (pseudo,)
    elif pseudo == None:
        cur.execute("SELECT id_user FROM USERS")
        conn.commit()
        check = (id_user,)
    else:
        cur.execute("SELECT name, id_user FROM USERS")
        conn.commit()
        check = (pseudo, id_user)
    if check in cur.fetchall():        
        commitcur()
        return True
    else:
        commitcur()
        return False
    
#suppression d'un compte
def suppression_compte(id_user):
    initcur()
    if check_compte(None, id_user):
        return False
    cur.execute('DELETE FROM USERS WHERE id_user = ?', (id_user,))
    commitcur()
    return True

def modification_pseudo(nv_pseudo, id_user):
    if check_compte(nv_pseudo):
        return False
    initcur()
    cur.execute('UPDATE USERS SET name = ? WHERE id_user = ?', (nv_pseudo, id_user))
    commitcur()
    return True

#connection
def connexion(pseudo, mdp):
    initcur()
    cur.execute("SELECT id_user FROM USERS WHERE name = ? AND password = ?", (pseudo, mdp))
    conn.commit()
    ans = cur.fetchall()
    commitcur()
    if len(ans) == 0:
        return False
    else:
        return ans[0][0]

#creation des posts
def creation_post(id_user, text):
    nv = (id_user,text, 0)
    initcur()
    cur.execute("INSERT INTO POSTS(id_user,text, likes) VALUES(?, ?, ?)", nv)
    commitcur()
    return True

#suppression d'un post
def suppression_post(id_post):
    initcur()
    cur.execute('DELETE FROM POSTS WHERE id_post = ?', (id_post,))
    commitcur()
    return True

#voir tout les posts
def voir_posts(n=0):
    initcur()
    cur.execute("SELECT id_post, text, id_user FROM POSTS")
    conn.commit()
    ans = cur.fetchall()
    commitcur()
    if n <= 0:
        return ans
    else:
        return ans [:n]

#obtention de tout les comptes
def voir_comptes(voir_id=False):
    initcur()
    if voir_id:
        cur.execute("SELECT id_user, name FROM USERS")
    else:
        cur.execute("SELECT name FROM USERS")
    conn.commit()
    ans = cur.fetchall()
    commitcur()
    return ans

#recherche des posts d'un user
def cherche_post(id_user):
    initcur()
    cur.execute("SELECT id_post, text, id_user FROM POSTS WHERE id_user = ?", (id_user,))
    conn.commit()
    ans = cur.fetchall()
    commitcur()
    return ans

#suppression des posts par suppression du compte
def del_posts(id_user):
    ans = cherche_post(id_user)
    for post in ans:
        suppression_post(post[0])
    return True

#creation likes
def ajouter_like(id_user, id_post):
    if not check_like(id_user, id_post):
        initcur()
        cur.execute("INSERT INTO LIKES(id_user, id_post) VALUES(?, ?)", (id_user, id_post))
        cur.execute('UPDATE POSTS SET likes = likes + 1 WHERE id_post = ?', (id_post,))
        commitcur()
        return True
    else: 
        return False

#suppression likes
def suppression_like(id_user, id_post):
    if check_like(id_user, id_post):
        initcur()
        cur.execute("DELETE FROM LIKES WHERE id_user = ? AND id_post = ?", (id_user, id_post))
        cur.execute('UPDATE POSTS SET likes = likes - 1 WHERE id_post = ?', (id_post,))
        commitcur()
        return True
    else: 
        return False

# check si un like existe
def check_like(id_user, id_post):
    initcur()
    cur.execute("SELECT * FROM LIKES WHERE id_user = ? AND id_post = ?", (id_user, id_post))
    conn.commit()
    if len(cur.fetchall()) > 0:
        commitcur()
        return True
    else: 
        commitcur()
        return False

#creation commentaire
def creation_commentaire(id_user, id_post, text):
    initcur()
    cur.execute("INSERT INTO COMMENTS(id_user, id_post, text) VALUES(?, ?, ?)", (id_user, id_post, text))
    commitcur()
    return True

#suppression commentaire
def suppression_commentaire(id_comment):
    initcur()
    cur.execute("DELETE FROM COMMENTS WHERE id_comment = ?", (id_comment,))
    commitcur()
    return True

#voir tout les commentaires
def voir_commentaires(id_post=None, id_user=None):
    initcur()
    if not id_post == None and not id_user == None:
        cur.execute("SELECT id_comment, text , id_user , id_post FROM COMMENTS WHERE id_user = ? AND id_post = ?", (id_user, id_post))
    elif id_post == None and not id_user == None:
        cur.execute("SELECT id_comment, text , id_user , id_post FROM COMMENTS WHERE id_user = ?", (id_user,))
    elif not id_post == None and id_user == None:
        cur.execute("SELECT id_comment, text , id_user , id_post FROM COMMENTS WHERE id_post = ?", (id_post,))
    else:
        cur.execute("SELECT id_comment, text , id_user , id_post FROM COMMENTS")
    conn.commit()
    ans = cur.fetchall()
    commitcur()
    return ans

# check si un commentaire existe
def check_commentaire(id_comment):
    initcur()
    cur.execute("SELECT * FROM COMMENTS WHERE id_comment = ?", (id_comment,))
    conn.commit()
    if len(cur.fetchall()) > 0:
        commitcur()
        return True
    else:
        commitcur()
        return False

def return_posts(n=3):
    li = voir_posts()
    ans = li[:-n]
    random.shuffle(ans)
    li = li[-n:]
    li.reverse()
    return li + ans

# #Ajout d'un nouveau livre à LIVRE:
# nvx_data = ('Hypérion','Simmons',1989,8)
# cur.execute("INSERT INTO LIVRES(titre,auteur,ann_publi,note) VALUES(?, ?, ?, ?)", nvx_data) #insertion du livre
# """
# #Modification d'une donnée de LIVRE
# modif = (7, 'Hypérion')
# cur.execute('UPDATE LIVRES SET note = ? WHERE titre = ?', modif) #modification

# #Suppression d'un livre dans la base de données
# suppr = ('Hypérion',)
# cur.execute('DELETE FROM LIVRES WHERE titre = ?', suppr) #suppression

# #Recherche des livres publié avant 1960 avec une note supérieur à 8
# recherche = (1960, 8)
# cur.execute('SELECT titre FROM LIVRES WHERE ann_publi < ? AND note > ?', recherche) #recherche
# """
# conn.commit() #envoie des modifications à la base de données

# liste = cur.fetchall() #liste des livres séléctionnés
# #print (liste)

# #Fin du programme:
# cur.close()
# conn.close()