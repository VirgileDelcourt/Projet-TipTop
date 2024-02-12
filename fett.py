###############################################################################
###                         TIP TOP (FRONT END)                             ###
###############################################################################

from tkinter import Tk, Frame, Button, Entry, Label, YES, messagebox,ttk
import tkinter as tk
from functools import partial
import sqlite3

#Connexion titop_backend:
from bett import connexion as fct_connexion
from bett import creation_compte as fct_creation_compte
from bett import creation_post as fct_my_post
from bett import return_posts as fct_post
from bett import initcur
from bett import commitcur

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
###############################################################################
##                                FENETRE                                    ##
###############################################################################

fenetre = Tk()
fenetre.title("TIP TOP")
fenetre.geometry("1110x620")
fenetre.minsize(1110,620)
background="#fce6f6"
fenetre.config(bg=background)

###############################################################################
##                                 BOITES                                    ##
###############################################################################

'_____________________________________________________________________________'

'                                  MENU                                       '
'_____________________________________________________________________________'

menu = Frame(fenetre, bg=background)

#Titre de la boite
titre = Label(menu, text="TIP TOP", font=("Consolas",50), bg=background, fg="black")
titre.pack(pady=45)

def retour_menu():
    menu.pack(expand=YES)
    connexion.pack_forget()
    creation_compte.pack_forget()
    compte.pack_forget()
    my_post.pack_forget()
    post.pack_forget()
    my_comment.pack_forget()
    comment.pack_forget()

'_____________________________________________________________________________'

'                               CONNEXION                                     '
'_____________________________________________________________________________'

connexion = Frame(fenetre, bg=background)
titre_connect = Label(connexion, text="Vous êtes déjà connecté", font=("Consolas",10), bg=background, fg="black")
#Titre de la boite
titre = Label(connexion, text="Connexion", font=("Consolas",20), bg=background, fg="black")
titre.pack(pady=45)

#Entrees:
nom = tk.StringVar()
nom.set("Nom")
#entree_1 = Entry(connexion, textvariable=nom, font=("Helvetica",15), bg=background, fg="black", width=30)
#entree_1.pack(pady=10)
initcur()
cur.execute('SELECT name FROM USERS')
conn.commit()
liste_nom = cur.fetchall()
listeChoix = ttk.Combobox(connexion, width = 40, textvariable = nom, values=liste_nom)

listeChoix.current()
listeChoix.pack()

mdp = tk.StringVar()
mdp.set("Mot de passe")
entree_2 = Entry(connexion, textvariable=mdp, font=("Helvetica",15), bg=background, fg="black", width=30)
entree_2.pack(pady=10)

def fe_connexion():
    if fct_connexion(nom.get(),mdp.get()) == False:
        messagebox.showerror('Erreur', "Le Nom ou le mot de passe est incorrect")
    else:
        titre_connect.pack(padx=10) 
        menu.pack(expand=YES)
        connexion.pack_forget()
        titre.config(text=nom.get())
        fct_connexion(nom.get(),mdp.get())
            
    return nom.get()

def id_user():
    return fct_connexion(nom.get(),mdp.get())

'''
    b_connexion.pack_forget()
    b_connexion = Button(menu, text=id, font=("Consolas",15), bg="white", fg="black", command=afficher_connexion, width=75)
    b_connexion.pack()
'''

bouton4 = Button(connexion, text="Connexion", font=("Helvetica",15), bg=background, fg="black", command=fe_connexion)
bouton4.pack(pady=10)

#Bouton du menu vers la boite:
def afficher_connexion():
    connexion.pack(expand=YES)
    menu.pack_forget()
b_connexion = Button(menu, text="Connexion", font=("Consolas",15), bg="white", fg="black", command=afficher_connexion, width=75)
b_connexion.pack(pady=10)

#Bouton retour vers le menu:
b_retour1 = Button(connexion, text="Retour", font=("Consolas",15), bg="white", fg="black", command=retour_menu, width=35)
b_retour1.pack()

#Retour vers la boite 'connexion'
def retour_connexion():
    connexion.pack(expand=YES)
    creation_compte.pack_forget()

'_____________________________________________________________________________'

'                            CREATION_COMPTE                                  '
'_____________________________________________________________________________'

creation_compte = Frame(fenetre, bg=background)
titre_crea = Label(creation_compte, text="Votre compte est créé", font=("Consolas",10), bg=background, fg="black")
#Titre de la boite
titre = Label(creation_compte, text="Créer un compte", font=("Consolas",20), bg=background, fg="black")
titre.pack(pady=45)

#Entrees:
crea_nom = tk.StringVar()
crea_nom.set("Nom")
entree_1 = Entry(creation_compte, textvariable=nom, font=("Helvetica",15), bg=background, fg="black", width=30)
entree_1.pack(pady=10)

crea_mdp = tk.StringVar()
crea_mdp.set("Mot de passe")
entree_2 = Entry(creation_compte, textvariable=mdp, font=("Helvetica",15), bg=background, fg="black", width=30)
entree_2.pack(pady=10)

mdp_v = tk.StringVar()
mdp_v.set("Mot de passe")
entree = Entry(creation_compte, textvariable=mdp_v, font=("Helvetica",15), bg=background, fg="black", width=30)
entree.pack(pady=10)

def fe_creation_compte():
    if mdp.get()!=mdp_v.get(): return False
    fct_creation_compte(nom.get(),mdp.get())
    titre_crea.pack()

bouton4 = Button(creation_compte, text="Creer un compte", font=("Helvetica",15), bg=background, fg="black", command=fe_creation_compte)
bouton4.pack(pady=10)

#Bouton du menu vers la boite:
def afficher_creation_compte():
    creation_compte.pack(expand=YES)
    connexion.pack_forget()
b_creation_compte = Button(connexion, text="Créer un compte", font=("Helvetica",15), bg=background, fg="black", command=afficher_creation_compte)
b_creation_compte.pack(pady=10)

#Bouton retour vers le menu:
b_retour2 = Button(creation_compte, text="Retour", font=("Consolas",15), bg="white", fg="black", command=retour_connexion, width=35)
b_retour2.pack(pady=10)

'_____________________________________________________________________________'

'                                COMPTE                                       '
'_____________________________________________________________________________'

compte = Frame(fenetre, bg=background)
'''
speudo=nom.get()
if speudo== "Nom":
    texte="Veuillez vous connecter"
else:
    texte=speudo    
titre = Label(compte, text=texte, font=("Consolas",20), bg=background, fg="black")
titre.pack(pady=45)

identifiant=nom.get()
titre = Label(compte, text=identifiant, font=("Consolas",20), bg=background, fg="black")
titre.pack(pady=45)
'''
#Informations perso
titre_bio = Label(compte, text="biographie", font=("Consolas",20), bg=background, fg="black")
titre_bio.pack(pady=45)

bio = tk.StringVar()
bio.set("Vous pouvez me modifier")
entree = Entry(compte, textvariable=bio, font=("Helvetica",15), bg=background, fg="black", width=30) #creation du champs qui contient la variable
entree.pack(pady=10)

def changer_bio():
    titre_bio.config(text=bio.get())
bouton4 = Button(compte, text="Cliquez pour actualiser", font=("Helvetica",15), bg=background, fg="black",width=30, command = changer_bio) #l'utilisateur peut actualiser le titre
bouton4.pack(pady=10)

#Bouton du menu vers la boite:
def afficher_compte():
    compte.pack(expand=YES)
    menu.pack_forget()
b_compte = Button(menu, text="Compte", font=("Consolas",15), bg="white", fg="black", command=afficher_compte, width=75)    
b_compte.pack(pady=10)

#Bouton retour vers le menu:
b_retour3 = Button(compte, text="Retour", font=("Consolas",15), bg="white", fg="black", command=retour_menu, width=35)
b_retour3.pack(pady=10)

'_____________________________________________________________________________'

'                                MY_POST                                      '
'_____________________________________________________________________________'

my_post = Frame(fenetre, bg=background)

#Titre de la boite
titre1 = Label(my_post, text="Mes publications", font=("Consolas",20), bg=background, fg="black")
titre1.pack(pady=45)

#Contenu de la publication
publication = Label(my_post, text=" ", font=("Helvetica",15), bg=background, fg="black")
publication.pack(pady=45)

#Champs pour publier
e_publication = tk.StringVar()
e_publication.set("Publication:")
entree = Entry(my_post, textvariable=e_publication, font=("Helvetica",15), bg=background, fg="black", width=30)
entree.pack(pady=45)


#Bouton pour publier
def publier():
    if id_user()==False:
        messagebox.showerror('Erreur', "Vous devez être connecté pour pouvoir poster")
    else:
        publication.config(text=e_publication.get())
        fct_my_post(id_user(),e_publication.get())

bouton4 = Button(my_post, text="Publier", font=("Helvetica",15), bg=background, fg="black", command=publier)
bouton4.pack(pady=10)

#Bouton du menu vers la boite:
def afficher_my_post():
    my_post.pack(expand=YES)
    menu.pack_forget()
b_my_post = Button(menu, text="Mes publications", font=("Consolas",15), bg="white", fg="black", command=afficher_my_post, width=75)    
b_my_post.pack(pady=10)

#Bouton retour vers le menu:
b_retour4 = Button(my_post, text="Retour", font=("Consolas",15), bg="white", fg="black", command=retour_menu, width=35)
b_retour4.pack(pady=10)

'_____________________________________________________________________________'

'                                 POST                                        '
'_____________________________________________________________________________'

post = Frame(fenetre, bg=background)

#Titre de la boite
titre = Label(post, text="Voir les publications", font=("Consolas",20), bg=background, fg="black")
titre.pack(pady=45)

post1=Label(post, text="", font=("Consolas",10), bg=background, fg="black")
post2=Label(post, text="", font=("Consolas",10), bg=background, fg="black")
post3=Label(post, text="", font=("Consolas",10), bg=background, fg="black")

rang = -1
posts = fct_post()
def afficher_publication():
    global rang
    global posts
    post1.config(text=posts[rang][1])
    if rang+1 < len(posts):
        post2.config(text=posts[rang+1][1])
    if rang+2 < len(posts):
        post3.config(text=posts[rang+2][1])
    post1.pack()
    post2.pack()
    post3.pack()

def augmenter_rang():
    global rang
    rang+=1
    afficher_publication()

def diminuer_rang():
    global rang
    rang-=1
    afficher_publication()

b_suivant = Button(post, text="->", font=("Consolas",15), bg="white", fg="black", command=augmenter_rang, width=25)    
b_suivant.pack(pady=10)

b_precedent = Button(post, text="<-", font=("Consolas",15), bg="white", fg="black", command=diminuer_rang, width=25)    
b_precedent.pack(pady=10)
#Bouton du menu vers la boite:
def afficher_post():
    post.pack(expand=YES)
    menu.pack_forget()
b_post = Button(menu, text="Voir les publications", font=("Consolas",15), bg="white", fg="black", command=afficher_post, width=75)    
b_post.pack(pady=10)

#Bouton retour vers le menu:
b_retour5 = Button(post, text="Retour", font=("Consolas",15), bg="white", fg="black", command=retour_menu, width=35)
b_retour5.pack(pady=10)

#Retour vers la boite 'post'
def retour_post():
    post.pack(expand=YES)
    my_comment.pack_forget()
    comment.pack_forget()
'_____________________________________________________________________________'

'                               MY_COMMENT                                    '
'_____________________________________________________________________________'

my_comment = Frame(fenetre, bg=background)

#Titre de la boite
titre = Label(my_comment, text="Commenter", font=("Consolas",20), bg=background, fg="black")
titre.pack(pady=10)

#Contenu du commentaire
commentaire = Label(my_comment, text=" ", font=("Helvetica",15), bg=background, fg="black")
commentaire.pack(pady=10)

#Champs pour commenter
e_commentaire = tk.StringVar()
e_commentaire.set("Commentaire:")
entree = Entry(my_comment, textvariable=e_commentaire, font=("Helvetica",15), bg=background, fg="black", width=30)
entree.pack(pady=10)

#Bouton pour commenter
def commenter():
    commentaire.config(text=e_commentaire.get())
bouton4 = Button(my_comment, text="Commenter", font=("Helvetica",15), bg=background, fg="black", command = commenter)
bouton4.pack(pady=10)
#Enregistrer le commentaire dans la base de données

#Bouton du menu vers la boite:
def afficher_my_comment():
    my_comment.pack(expand=YES)
    post.pack_forget()
b_my_comment = Button(post, text="Commenter", font=("Consolas",15), bg="white", fg="black", command=afficher_my_comment, width=75)    
b_my_comment.pack(pady=10)

#Bouton retour vers le menu:
b_retour6 = Button(my_comment, text="Retour", font=("Consolas",15), bg="white", fg="black", command=retour_post, width=35)
b_retour6.pack(pady=10)

'_____________________________________________________________________________'

'                                COMMENT                                      '
'_____________________________________________________________________________'

comment = Frame(fenetre, bg=background)

#Titre de la boite
titre = Label(comment, text="Voir les commentaires", font=("Consolas",20), bg=background, fg="black")
titre.pack(pady=45)

#Bouton du menu vers la boite:
def afficher_comment():
    comment.pack(expand=YES)
    post.pack_forget()
b_comment = Button(post, text="Voir les commentaires", font=("Consolas",15), bg="white", fg="black", command=afficher_comment, width=75)
b_comment.pack(pady=10)

#Bouton retour vers le menu:
b_retour7 = Button(comment, text="Retour", font=("Consolas",15), bg="white", fg="black", command=retour_post, width=35)
b_retour7.pack(pady=10)


menu.pack()
fenetre.mainloop()