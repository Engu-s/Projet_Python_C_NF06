from xlrd import* 
from pandas import*
import pandas as pds
import xlwt
import random
from xlwt import Workbook
from random import*
import numpy as np
import matplotlib.pyplot as plt
import os
import csv



def ajout_manuel(nb_produits,liste_produits):
  """
  Cette fonction va créer OU rajouter des produits qui vont composer le catalogue de la boutique. Ils seront rajoutés dans un tableur et dans deux listes.

  Args:
      nb_produits (entier): Variable qui sera incrémentée et qui correspond initialement à la ligne où est placé le dernier produit dans le tableur
      liste_produits (liste de dictionnaires ): Correspond au catalogue initial des produits quand la fonction est appelée
  Returns:
      produits_recup (DataFrame): Correspond au contenu du tableur qui a été récupéré 
      liste_produits (liste de dictionnaires): Correspond au catalogue final des produits
      nb_produits (entier): Indice correspondant à la ligne du dernier produit créé par la fonction
  """
  arret = '0'
  while (arret == '0'):
    produit={'UID': int, 'Nom' : str , 'Prix': float, 'Poids' : float, 'Categories' : str, 'Marque': str, 'Annee':int,'Quantite': int, 'Nb_commandes': int, 'Avis' : float}
    print("Ecrivez les caracteristiques du produit")
    nb_produits = nb_produits + 1                  
    produit['UID'] = nb_produits
    produit['Nom'] = str(input("Nom du produit\n"))
    produit['Prix'] = float(input("Prix du produit en euros\n"))          
    produit['Poids'] = float(input("Poids du produit en kg\n"))          
    print("Ecrivez le chiffre correspondant à la catégorie du produit \n1. Ordinateur \n2. Téléphone \n3. Tablette \n4. Appareil photo \n5. Enceinte \n6. Autre")
    choix = int(input())
    if (choix==1):
      produit['Categories'] = str("Ordinateur")
    if (choix==2):
      produit['Categories'] = str("Téléphone")
    if (choix==3):
      produit['Categories'] = str("Tablette")
    if (choix==4):
      produit['Categories'] = str("Appareil photo")
    if (choix==5):
      produit['Categories'] = str("Enceinte")
    if (choix==6):
      produit['Categories'] = str(input("Ecrivez la catégorie recherchée \n"))          
    print("Ecrivez le chiffre associé a la marque du produit \n1. Apple \n2. Samsung \n3. Asus \n4. Logitech \n5. HP \n6. Autre")
    choix = int(input())
    if (choix==1):
      produit['Marque'] = str("Apple")
    if (choix==2):
      produit['Marque'] = str("Samsung")
    if (choix==3):
      produit['Marque'] = str("Asus")
    if (choix==4):
      produit['Marque'] = str("Logitech")
    if (choix==5):
      produit['Marque'] = str("HP")
    if (choix==6):
      produit['Marque'] = str(input("Ecrivez la marque recherchée \n"))           
    produit['Annee'] = int(input("Année de sortie du produit \n"))          
    produit['Quantite'] = int(input("Quantité de produits disponibles  \n"))          
    produit['Nb_commandes'] = int(input("Nombre de commandes en attentes \n"))          
    print("Ecrivez le nombre associé à votre opinion du produit \n1. Pas du tout satisfait \n2. Peu satisfait \n3. Plutot satisfait \n4. Bien satisfait \n5. Entièrement satisfait")
    choix = float(input())
    produit['Avis'] = float(choix)       
    liste_produits.append(produit)         
    ficheprod.write(nb_produits, 0, produit['UID']);ficheprod.write(nb_produits, 1, produit['Nom']);ficheprod.write(nb_produits, 2, produit['Prix']);ficheprod.write(nb_produits, 3, produit['Poids']);ficheprod.write(nb_produits, 4, produit['Categories']);ficheprod.write(nb_produits, 5, produit['Marque']);ficheprod.write(nb_produits, 6, produit['Annee']);ficheprod.write(nb_produits, 7, produit['Quantite']);ficheprod.write(nb_produits, 8, produit['Nb_commandes']);ficheprod.write(nb_produits, 9, produit['Avis'])
    Recapitulatif.save('Recaproduits.xls')
    arret=str(input("Tapez 0 pour continuer a ajouter des produits \n"))
  print("Catalogue complet des produits :")
  produits_recup = pds.read_excel("Recaproduits.xls")
  print(produits_recup)
  return(produits_recup,liste_produits,nb_produits)
    


def ajout_aleatoire():
  """
  Cette fonction va créer aléatoirement un nombre choisit de produits qui vont composer le catalogue de la boutique. Ils seront rajoutés dans un tableur et dans deux listes.

  Args:
      NONE
  Returns:
      produits_recup (DataFrame): Correspond au contenu du tableur qui a été récupéré 
      liste_produits (liste de dictionnaires): Correspond au catalogue final des produits
      nb_produits (entier): Indice correspondant à la ligne du dernier produit créé par la fonction
  """
  nb_produits=int(input("Choisissez le nombre de produits "))
  for i in range (nb_produits):
    # Valeurs pour chaque produit générées une à une (souvent aléatoirement) 
    produit={'UID': int(i+1), 'Nom' : str(i+1) , 'Prix': round((uniform(5,1000)),1), 'Poids' : round((uniform(5,1000)),1), 'Categories' : str, 'Marque': str, 'Annee':randint(2000,2022),'Quantite': randint(1,100), 'Nb_commandes': randint(1,100), 'Avis' : round((uniform(1,5)),1)}
    # La marque sera choisie aléatoirement parmi les 5 déjà existantes
    choix = randint(1,5)
    if (choix==1):
      produit['Marque'] = str("Apple")
    if (choix==2):
      produit['Marque'] = str("Samsung")
    if (choix==3):
      produit['Marque'] = str("Asus")
    if (choix==4):
      produit['Marque'] = str("Logitech")
    if (choix==5):
      produit['Marque'] = str("HP")
    # La catégorie sera choisie aléatoirement parmi les 5 déjà existantes
    choix = randint(1,5)
    if (choix==1):
      produit['Categories'] = str("Ordinateur")
    if (choix==2):
      produit['Categories'] = str("Téléphone")
    if (choix==3):
      produit['Categories'] = str("Tablette")
    if (choix==4):
      produit['Categories'] = str("Appareil photo")
    if (choix==5):
      produit['Categories'] = str("Enceinte")
    # Le produit créé est ajouté au catalogue des produits déjà existants     
    liste_produits.append(produit) 
    # Les caractéristiques du produit créé sont ajoutées au tableau Excel 
    ficheprod.write(i+1, 0, produit['UID']);ficheprod.write(i+1, 1, produit['Nom']);ficheprod.write(i+1, 2, produit['Prix']);ficheprod.write(i+1, 3, produit['Poids']);ficheprod.write(i+1, 4, produit['Categories']);ficheprod.write(i+1, 5, produit['Marque']);ficheprod.write(i+1, 6, produit['Annee']);ficheprod.write(i+1, 7, produit['Quantite']);ficheprod.write(i+1, 8, produit['Nb_commandes']);ficheprod.write(i+1, 9, produit['Avis'])
    Recapitulatif.save('Recaproduits.xls')
  print("Catalogue complet des produits :")
  # Affiche tout le catalogue provenant du fichier Excel
  produits_recup = pds.read_excel("Recaproduits.xls")
  print(produits_recup)
  return(produits_recup,liste_produits,nb_produits)
  


def trie_catalogue(liste_produits):
  """
  Cette fonction va trier le catalogue de la boutique en fonction de filtres que l'utilisateur va choisir et afficher tous les produits respectant ces conditions.

  Args:
      liste_produits (liste de dictionnaires ): Correspond au catalogue des produits au moment où la fonction est appelée
  Returns:
      NONE
  """
  print(produits_recup)
  filtre = '0'
  filtre_categorie=str('-1')
  filtre_marque=str('-1')
  filtre_annee=int('-1')
  filtre_nb_commandes=int('-1')
  filtre_quantite=int('-1')
  filtre_avis=float('-1')
  print("Quel paramètre du produit souhaitez vous filtrer ? \n1. Sa catégorie \n2. Sa marque \n3. Son année minimale de sortie \n4. Son nombre minimum de commandes \n5. Sa quantité minimale encore en stock \n6. Sa note moyenne des avis client")         
  # Boucle permettant de filtrer tout ce que l'on veut sur le produit
  while (filtre=='0'):
    choix_filtre = str(input())
    # Condition pour trier la catégorie
    if (choix_filtre=='1'):
      print("Rappel des catégories proposées par défaut : Ordinateur / Téléphone / Tablette / Appareil photo / Enceinte \nEcrivez en toutes lettres celle qui vous intéresse")
      filtre_categorie = str(input("Indiquez la catégorie souhaitée pour ce produit "))
    # Condition pour trier la marque          
    if (choix_filtre=='2'):
      print("Rappel des marques proposées par défaut : Apple / Samsung / Asus / Logitech / HP \nEcrivez en toutes lettres celle qui vous intéresse")
      filtre_marque = str(input("Indiquez la marque souhaitée pour ce produit "))  
    # Condition pour trier l'année minimale             
    if (choix_filtre=='3'):
      filtre_annee = int(input("Indiquez l'année minimale de sortie du produit "))  
    # Condition pour trier le nombre de commandes           
    if (choix_filtre=='4'):
      filtre_nb_commandes = int(input("Indiquez le nombre minimum de commandes du produit "))  
    # Condition pour trier la quantité disponible          
    if (choix_filtre=='5'):
      filtre_quantite = int(input("Indiquez en combien d'exemplaires le produit doit être disponible "))  
    # Condition pour trier l'avis moyen         
    if (choix_filtre=='6'):
      filtre_avis = float(input("Indiquez l'avis minimum du produit "))
    # Condition d'arrêt de la boucle
    filtre = str(input("Ecrivez 0 si vous souhaitez encore filtrer le catalogue "))
    if (filtre=='0'):
      print("Rappel des filtres : 1. Catégorie \n2. Marque \n3. Année \n4. Nombre de commandes \n5. Quantité disponible \n6. Avis clients ")
  # Crée une liste représentant la liste filtrée
  nouvelle_liste = []
  for i in range (len(liste_produits)) :
    correct = 0
    if ((filtre_categorie != '-1') and (liste_produits[i]['Categories'] != filtre_categorie)):
      correct=1
    if ((filtre_marque != '-1') and (liste_produits[i]['Marque'] != filtre_marque)):
      correct=1
    if ((filtre_annee != '-1') and (liste_produits[i]['Annee'] < filtre_annee)):
      correct=1
    if ((filtre_nb_commandes != '-1') and (liste_produits[i]['Nb_commandes'] < filtre_nb_commandes)):
      correct=1  
    if ((filtre_quantite != '-1') and (liste_produits[i]['Quantite'] < filtre_quantite)):
      correct=1
    if ((filtre_avis != '-1') and (liste_produits[i]['Avis'] < filtre_avis)):
      correct=1
    if (correct==0) :
      nouvelle_liste.append(liste_produits[i])              
  print("Voici la liste des produits répondant à vos critères")
  for loop in range (len(nouvelle_liste)):
    print(nouvelle_liste[loop])


        
def stats_marques(liste_produits):
  """
  Cette fonction va afficher les produits qui rapportent le plus puis le moins d'argent par marque et leurs valeurs respectives. 

  Args:
      liste_produits (liste de dictionnaires ): Correspond au catalogue des produits quand la fonction est appelée
  Returns:
      NONE
  """
  liste_marques=[]
  for i in range (len(liste_produits)):
    ajout=1
    for j in range (len(liste_marques)):
      if (liste_marques[j] == liste_produits[i]['Marque']):
        ajout = 0
    if ajout==1:
      liste_marques.append(liste_produits[i]['Marque'])
  print(liste_marques)
  liste_resultat_best = []
  liste_benefs = []
  for i in range (len(liste_marques)):
    benef_max=0 
    for j in range (len(liste_produits)):
      if (liste_produits[j]['Marque'] == liste_marques[i] and benef_max==0):
        maximum = liste_produits[j]
        benef_max = round((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix']))
      elif (((liste_produits[j]['Marque']) == (liste_marques[i])) and benef_max != 0 ):
        if (int(benef_max) < round(((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix'])))):
          benef_max = round((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix']))
          maximum = liste_produits[j]
    if (benef_max != 0):
      liste_resultat_best.append(maximum)
      liste_benefs.append(benef_max)
  print("Les meilleurs produits par marques sont: \n")
  for i in range (len(liste_resultat_best)):
    print("UID du meilleur produit",liste_resultat_best[i]['Marque'],":",liste_resultat_best[i]['UID'])
  print("\nIls ont respectivement rapporté:")
  for i in range (len(liste_resultat_best)):
    print(liste_benefs[i],"euros")
  liste_resultat_pire = []
  liste_benefs = []
  for i in range (len(liste_marques)):
    benef_min=0
    for j in range (len(liste_produits)):
      if (liste_produits[j]['Marque'] == liste_marques[i] and benef_min==0):
        minimum = liste_produits[j]
        benef_min = round((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix']))
      elif (((liste_produits[j]['Marque']) == (liste_marques[i])) and benef_min != 0 ):
        if (int(benef_min) > round(((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix'])))):
          benef_min = round((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix']))
          minimum = liste_produits[j]
    if (benef_min != 0):
      liste_resultat_pire.append(minimum)
      liste_benefs.append(benef_min)
  print("Les pires produits par marques sont:\n")
  for i in range (len(liste_resultat_pire)):
    print("UID du pire produit",liste_resultat_pire[i]['Marque'],":",liste_resultat_pire[i]['UID'])
  print("\nIls ont respectivement rapporté:")
  for i in range (len(liste_resultat_pire)):
    print(liste_benefs[i],"euros")



def stats_categories(liste_produits):
  """
  Cette fonction va afficher les produits qui rapportent le plus puis le moins d'argent par catégorie et leurs valeurs respectives. 

  Args:
      liste_produits (liste de dictionnaires ): Correspond au catalogue des produits quand la fonction est appelée
  Returns:
      NONE
  """
  liste_categories=[]
  for i in range (len(liste_produits)):
    ajout=1
    for j in range (len(liste_categories)):
      if (liste_categories[j] == liste_produits[i]['Categories']):
        ajout = 0
    if ajout==1:
      liste_categories.append(liste_produits[i]['Categories'])
  print(liste_categories)
  liste_resultat_best = []
  liste_benefs = []
  for i in range (len(liste_categories)):
    benef_max=0 
    for j in range (len(liste_produits)):
      if (liste_produits[j]['Categories'] == liste_categories[i] and benef_max==0):
        maximum = liste_produits[j]
        benef_max = round((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix']))
      elif (((liste_produits[j]['Categories']) == (liste_categories[i])) and benef_max != 0 ):
        if (int(benef_max) < round(((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix'])))):
          benef_max = round((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix']))
          maximum = liste_produits[j]
    if (benef_max != 0):
      liste_resultat_best.append(maximum)
      liste_benefs.append(benef_max)
  print("Les meilleurs produits par catégories sont:\n")
  for i in range (len(liste_resultat_best)):
    print("UID du meilleur produit de la catégorie",liste_resultat_best[i]['Categories'],":",liste_resultat_best[i]['UID'])
  print("\nIls ont respectivement rapporté:")
  for i in range (len(liste_resultat_best)):
    print(liste_benefs[i],"euros")
  liste_resultat_pire = []
  liste_benefs = []
  for i in range (len(liste_categories)):
    benef_min=0 
    for j in range (len(liste_produits)):
      if (liste_produits[j]['Categories'] == liste_categories[i] and benef_min==0):
        minimum = liste_produits[j]
        benef_min = round((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix']))
      elif (((liste_produits[j]['Categories']) == (liste_categories[i])) and benef_min != 0 ):
        if (int(benef_min) > round(((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix'])))):
          benef_min = round((liste_produits[j]['Nb_commandes'])*(liste_produits[j]['Prix']))
          minimum = liste_produits[j]
    if (benef_min != 0):
      liste_resultat_pire.append(minimum)

      liste_benefs.append(benef_min)
  print("Les pires produits par catégories sont:\n")
  for i in range (len(liste_resultat_pire)):
    print("UID du pire produit de la catégorie",liste_resultat_pire[i]['Categories'],":",liste_resultat_pire[i]['UID'])
  print("\nIls ont respectivement rapporté:")
  for i in range (len(liste_resultat_pire)):
    print(liste_benefs[i],"euros")



def total_ventes(liste_produits) :
  """
  Cette fonction va afficher la somme totale des revenus générés par les produits présents dans le catalogue. 

  Args:
      liste_produits (liste de dictionnaires ): Correspond au catalogue des produits quand la fonction est appelée
  Returns:
      NONE
  """
  print("Nous calculons le total des ventes effectuées par le magasin : ")
  benef_max = int(0)
  for i in range (len(liste_produits)):
    benef_max = benef_max + ((liste_produits[i]['Prix']) * (liste_produits[i]['Nb_commandes']))
  print("Le magasin a vendu des produits pour une somme totale de {0:.2f}".format(benef_max),"euros \n")
  


def graph_nb_produits(liste_produits):
  """
  Cette fonction va générer un graphique correspondant au nombre de produits par catégorie. 

  Args:
      liste_produits (liste de dictionnaires ): Correspond au catalogue des produits quand la fonction est appelée
  Returns:
      NONE
  """
  liste_categories=[]
  for i in range (nb_produits):
    ajout=1
    for j in range (len(liste_categories)):
      if (liste_categories[j] == liste_produits[i]['Categories']):
        ajout = 0
    if ajout==1:
      liste_categories.append(liste_produits[i]['Categories'])
  plt.figure(2)
  liste_quantites=[]
  for loop in range (len(liste_categories)):
    somme_produits=0
    for i in range (nb_produits): 
      if (liste_categories[loop]==liste_produits[i]['Categories']):
        somme_produits = somme_produits + liste_produits[i]['Quantite']
    liste_quantites.append(somme_produits)
  print(liste_categories,liste_quantites)
  plt.bar(range(len(liste_quantites)),liste_quantites,bottom = 0 )
  compteur= []
  for i in range (len(liste_quantites)):
    compteur.append(i)
  plt.xticks(compteur, liste_categories)
  plt.title("Nombre de produits par catégorie")
  plt.legend()
  plt.show()



def graph_nb_commandes(liste_produits):
  """
  Cette fonction va générer un graphique correspondant au nombre de commandes par marque. 

  Args:
      liste_produits (liste de dictionnaires ): Correspond au catalogue des produits quand la fonction est appelée
  Returns:
      NONE
  """
  liste_marques=[]
  for i in range (nb_produits):
    ajout=1
    for j in range (len(liste_marques)):
      if (liste_marques[j] == liste_produits[i]['Marque']):
        ajout = 0
    if ajout==1:
      liste_marques.append(liste_produits[i]['Marque'])
  plt.figure(3)
  liste_quantites=[]
  for loop in range (len(liste_marques)):
    somme_produits=0
    for i in range (nb_produits): 
      if (liste_marques[loop]==liste_produits[i]['Marque']):
        somme_produits = somme_produits + liste_produits[i]['Nb_commandes']
    liste_quantites.append(somme_produits)
  print(liste_marques,liste_quantites)
  plt.bar(range(len(liste_quantites)),liste_quantites,bottom = 0 )
  compteur= []
  for i in range (len(liste_quantites)):
    compteur.append(i)
  plt.xticks(compteur, liste_marques)
  plt.title("Nombre de commandes par marque")
  plt.legend()
  plt.show()   


  
def livraison(produits_recup,liste_produits):
  """
  Cette fonction va générer une liste de produits à envoyer dans un camion de livraison. Elle sera stockée dans un tableur au format .csv

  Args:
      produits_recup (DataFrame): Correspond au contenu du tableur qui a été récupéré 
      liste_produits (liste de dictionnaires ): Correspond au catalogue des produits quand la fonction est appelée
  Returns:
      NONE
  """
  print("Vous êtes le responsable des produits à expédier, voici notre catalogue de produits :")
  print(produits_recup)
  livraison = '0'
  os.remove('Recaproduits.xls')
  Recapitulatif = Workbook()
  ficheprod = Recapitulatif.add_sheet('Liste des produits')
  ficheprod.write(0, 0, 'UID');ficheprod.write(0, 1, 'Nom');ficheprod.write(0, 2, 'Prix');ficheprod.write(0, 3, 'Poids');ficheprod.write(0, 4, 'Categories');ficheprod.write(0, 5, 'Marque');ficheprod.write(0, 6, 'Annee');ficheprod.write(0, 7, 'Quantite');ficheprod.write(0, 8, 'Nb_commandes');ficheprod.write(0, 9, 'Avis')
  article={'UID': int, 'Prix': float, 'Poids' : float,'Quantite': int,}
  liste_livraison = []
  while (livraison=='0'):
    article={'UID': int, 'Prix': float, 'Poids' : float,'Nb_commandes': int,}
    UID_livraison=int(input("Ecrivez l'UID du produit dont vous avez besoin : "))
    nb_commandes = int(input("Choisissez le nombre de commandes de votre produit : "))
    arret= 0
    for i in range (len(liste_produits)):
      if(liste_produits[i]['UID']==UID_livraison and arret==0):
        arret = 1
        article['UID'] = liste_produits[i]['UID']
        article['Poids'] = liste_produits[i]['Poids']
        article['Prix'] = liste_produits[i]['Prix']
        if (liste_produits[i]['Quantite'] < nb_commandes):
          article['Nb_commandes'] = liste_produits[i]['Quantite']
          liste_produits[i]['Quantite'] = 0
        else :
          article['Nb_commandes'] = nb_commandes
          liste_produits[i]['Quantite'] = liste_produits[i]['Quantite'] - nb_commandes
        liste_livraison.append(article)
    livraison = (str(input("Ecrivez 0 si vous souhaitez rajouter un autre produit à exporter ")))
  print("\nVoici la liste des objets à livrer :")
  for i in range (len(liste_livraison)):
    print(liste_livraison[i])
  tableur_livraison = pds.DataFrame(liste_livraison)
  print(tableur_livraison)
  tableur_livraison.to_csv('prod_livraison.csv', index=False, header=True)
  for i in range(len(liste_produits)):
      ficheprod.write(i+1, 0, liste_produits[i]['UID']);ficheprod.write(i+1, 1, liste_produits[i]['Nom']);ficheprod.write(i+1, 2, liste_produits[i]['Prix']);ficheprod.write(i+1, 3, liste_produits[i]['Poids']);ficheprod.write(i+1, 4, liste_produits[i]['Categories']);ficheprod.write(i+1, 5, liste_produits[i]['Marque']);ficheprod.write(i+1, 6, liste_produits[i]['Annee']);ficheprod.write(i+1, 7, liste_produits[i]['Quantite']);ficheprod.write(i+1, 8, liste_produits[i]['Nb_commandes']);ficheprod.write(i+1, 9, liste_produits[i]['Avis'])
      Recapitulatif.save('Recaproduits.xls')
  produits_recup = pds.read_excel("Recaproduits.xls")
  voir_nouv_liste= int(input("Tapez 0 si vous voulez voir la liste modifiée : "))
  if (voir_nouv_liste == 0):
    print(produits_recup)
    
  
def recup_camion():
  """
  Cette fonction va lire un fichier .txt pour créer la liste des UID et leurs quantités respectives stockées dans le camion de livraison.

  Args:
      NONE
  Returns:
      NONE
  """
  camion = open("livraison_camion.txt", "r")
  data = camion.read()
  liste_camion = data.split("\n")
  camion.close()  
  liste_UID=[]
  for i in range (0,len(liste_camion)):
    ajout=1
    for j in range (len(liste_UID)):
      if (liste_UID[j] == liste_camion[i]):
        ajout = 0
    if ajout==1 and liste_camion[i] !='':
      liste_UID.append(liste_camion[i])
  
  liste_finale_livr = []
  for i in range (len(liste_UID)):
    nb_UID = 0 
    for j in range (len(liste_camion)):
      if (liste_camion[j] == liste_UID[i]):
       nb_UID = nb_UID + 1
    liste_finale_livr.append(nb_UID)
  print("Livraison prioritaire du camion: ")
  for i in range (len(liste_UID)):
    if (liste_finale_livr[i]==1):
      print("Le produit à l'UID ",liste_UID[i],"en",liste_finale_livr[i],"exemplaire")
    else :
      print("Le produit à l'UID ",liste_UID[i],"en",liste_finale_livr[i],"exemplaires")
  
  

def service_client():
  """
  Cette fonction va clarifier les différents rôles pouvant être sélectionnés par l'utilisateur et proposées d'autres fonctionnalités divertissantes.

  Args:
      NONE
  Returns:
      NONE
  """
  serv_client = 0
  print("\nBonjour, vous êtes bien sur notre service client, voici les aides qui sont à votre disposition : \n1. Détails sur le rôle du visiteur \n2. Détails sur le rôle du manager \n3. Détails sur le rôle du responsable \n4. Générateur de blagues aléatoires \n5. Retour au menu principal ") 
  while (serv_client != 5):
    serv_client=int(input("Tapez le numéro correspondant à votre demande, sinon, tapez 5 pour fermer notre service client  " ))
    if (serv_client==1) : 
      print("\nLe visiteur représente un client naviguant librement sur notre site e-commerce. \n Il a accès à tous les produits proposés mais ne peut pas les manipuler. Il faut de préférence au préalable qu'un catalogue ait été créé par le manager.")  
    if (serv_client==2) :
      print("\nLe manager s'occupe des stocks des produits de l'entreprise. \n C'est à lui de définir les produits présents dans le catologue. Il également peut le filtrer et l'utiliser pour afficher des données.")
    if (serv_client==3) :
      print("\nLe responsable va saisir les listes de produits à expédier à partir d'un catalogue déjà existant. \n De ce fait, il faut au préalable que le manager se soit occupé des stocks. Lorsque la livraison aura été effectuée, il pourra également inspecter le contenu du camion de livraison.")
    if (serv_client == 4) :
      blague=int(randint(1,10))
      if (blague==1):
        print("\nQue fait une fraise sur un cheval ? \n \n Tagada tagada")
      if (blague==2):
        print("\nUn sinus tombe à l'eau et devient un cosinus, pourquoi ? \n \n Parce qu'il a dérivé ! #MT01 #Secondjury")
      if (blague==3):
        print("\nQuel est la divinité la plus connectée ? \n \n La déesse L (L'ADSL)")
      if (blague==4):
        print("\nQuel est le fruit préféré de la vache ? \n \n LE MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEUHLON")
      if (blague==5):
        print("\nQuel est l'animal le plus connecté ? \n \n Le porc USB")
      if (blague==6):
        print("\nComment est-ce que les abeilles communiquent entre elles ? \n \n Par e-miel")
      if (blague==7):
        print("\nEst-ce qu'une poule peut parler anglais ? \n \n Yes chicken (she can)")
      if (blague==8):
        print("\nQuelle princesse a les lèvres gercées ? \n \n Labello bois dormant")
      if (blague==9):
        print("\nQue fait un geek quand il a peur ? \n \n Il URL (hurle)")
      if (blague==10):
        print("\nQue fait un geek quand il descend du métro ? \n \n Il libère la RAM")
    if(serv_client==5):
      print("\nNous espérons avoir répondu à votre problème, au revoir! \n")



              
arret_programme=0
"""
Condition permettant de répéter indéfiniment le programme. Tant que cette variable est égale à 0, le programme continue.
"""
while (arret_programme == 0): 
  
  print("1. Visiteur \n2. Manager \n3. Responsable \n4. Service client")
  role = int(input("Indiquez le chiffre correspondant à votre rôle dans notre magasin e-commerce ")) 
  """
  Variable définissant l'utilisateur parmi une liste de rôles associés à des chiffres.
  """ 
  
  if(role == 1 and 'liste_produits' in globals()):
    print("Bonjour, voici notre catalogue de produits :")
    print(produits_recup) 
  elif(role == 1):
    print("Oups, il semblerait que notre catalogue ne soit pas accessible pour l'instant, veuillez en parler au manager.")
  
  
  if(role==2):
    print("Vous êtes le manager, choisissez l'action à réaliser en fonction du numéro associé \n1. Créer le catalogue de produits \n2. Rajouter de nouveaux produits au catalogue \n3. Trier le catalogue de produits \n4. Récupérer des statistiques du catalogue utiles")
    job_manager = str(input()) 
    """
    Variable permettant de définir le travail souhaité par le manager parmi une liste d'actions qui sont associées à des chiffres.
    """ 
    if (job_manager=='1'):  
      print("Comment voulez vous créer votre catalogue ? \n1. Manuellement \n2. Automatiquement")
      mode_production = int(input())
      """
      Variable permettant de définir la méthode d'ajout des produits dans le catalogue. Ces méthodes sont associées à des chiffres.
      """  
      liste_produits = [] 
      """
      Liste permettant de stocker des dictionnaires correspondant à des produits. Cette liste correspond au catalogue.
      """ 
      nb_produits = 0 
      produit={'UID': int, 'Nom' : str , 'Prix': float, 'Poids' : float, 'Categories' : str, 'Marque': str, 'Annee':int,'Quantite': int, 'Nb_commandes': int, 'Avis' : float}
      """
      Dictionnaire correspondant à la structure d'un produit de la boutique e-commerce
      """
      Recapitulatif = Workbook() 
      """
      Variable permettant de créer un tableau Excel qui sera complété par l'ajout des différents produits de la boutique.
      """
      ficheprod = Recapitulatif.add_sheet('Liste des produits') # Crée un fichier Excel vierge
      """ 
      Variable permettant de stocker des données qui seront transférées dans un tableau Excel.
      """ 

      ficheprod.write(0, 0, 'UID');ficheprod.write(0, 1, 'Nom');ficheprod.write(0, 2, 'Prix');ficheprod.write(0, 3, 'Poids');ficheprod.write(0, 4, 'Categories');ficheprod.write(0, 5, 'Marque');ficheprod.write(0, 6, 'Annee');ficheprod.write(0, 7, 'Quantite');ficheprod.write(0, 8, 'Nb_commandes');ficheprod.write(0, 9, 'Avis')  
      # Crée titres colonnes à la ligne 0 du fichier Excel    
      
    if ((job_manager=='1'and (mode_production==1)) or (job_manager=='2' and 'liste_produits' in globals())):
      (produits_recup,liste_produits,nb_produits) = ajout_manuel(nb_produits,liste_produits)
    elif (job_manager=='2'):
      print("Oups, il semblerait que notre catalogue ne soit pas accessible pour l'instant, vous devriez régler le problème monsieur le manager.")  
    if (job_manager=='1'and (mode_production==2)):
      (produits_recup,liste_produits,nb_produits) = ajout_aleatoire()
      
    if (job_manager=='3' and 'liste_produits' in globals()):
      trie_catalogue(liste_produits)
    elif (job_manager=='3'):
      print("Oups, il semblerait que notre catalogue ne soit pas accessible pour l'instant, vous devriez régler le problème monsieur le manager.")
      
    if (job_manager=='4' and 'liste_produits' in globals()):
      print("Tapez la statistique recherchée qui correspond au numéro indiqué : \n1. Meilleur/pire produit par marque en termes de ventes (en euros) \n2. Meilleur/pire produit par catégorie en termes de ventes (en euros) \n3. Total des ventes en euros réalisées par le magasin \n4. Graphique de nombre de produits par catégorie \n5. Graphique du total des ventes par marque de produits.")
      num_stat=int(input()) 
      """_summary_ Variable permettant de définir le choix de statistique à consulter par le manager parmi une liste qui est associée à des chiffres.
      """
      if (num_stat==1):
        stats_marques(liste_produits)
      if (num_stat==2):
        stats_categories(liste_produits)
      if (num_stat==3):
        total_ventes(liste_produits)
      if (num_stat==4):
        graph_nb_produits(liste_produits)
      if (num_stat==5):
        graph_nb_commandes(liste_produits)
    elif (job_manager=='4'):
      print("Oups, il semblerait que notre catalogue ne soit pas accessible pour l'instant, vous devriez régler le problème monsieur le manager.")
     
  if(role==3):
    print("Vous êtes le responsable, choisissez l'action à réaliser en fonction du numéro associé \n1. Créer une liste de produits à livrer \n2. Observer le contenu du camion")
    num_stat=int(input()) 
    if (num_stat==1 and 'liste_produits' in globals()):
      livraison(produits_recup,liste_produits)
    elif (num_stat==1):
       print("Oups, il semblerait que notre catalogue ne soit pas accessible pour l'instant, veuillez en parler au manager.")
    if (num_stat==2):
       recup_camion()
    elif (num_stat==2):
      print("Oups, il semblerait que nous n'ayons pas à livrer de produits pour l'instant, vous devriez en organiser une monsieur le responsable.")
 
   
    
  if(role==4):
    service_client()
  arret_programme=int(input("Tapez 0 pour continuer "))      
print("Merci d'avoir visité notre site e-commerce, nous vous souhaitons une bonne fin de journée !")    
