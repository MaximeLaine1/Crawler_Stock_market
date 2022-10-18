# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:22:54 2021

@author: laine
"""


from bs4 import BeautifulSoup
import requests
import time


###Crawler : collecter les donnees de Kering   
#boucle while 1ère heure et 40 min
    
after = time.time()+6000
listev1 = []
url = 'https://www.boursorama.com/cours/1rPKER/'

while time.time()< after :
    
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'lxml')
    
    test = soup.find('span', {'class':'c-instrument c-instrument--last'})

#valeur de l'action Kering
    v1 = test.text
    
   
    listev1.append(v1)
    print(v1)
    time.sleep(60)

print(listev1)

#boucle while 2ème période : 50min
    
after = time.time()+3000
listev2 = []
url = 'https://www.boursorama.com/cours/1rPKER/'

while time.time()< after :
    
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'lxml')
   
    test = soup.find('span', {'class':'c-instrument c-instrument--last'})
    
#    print(test)
#valeur de l'action Kering
    v1 = test.text
    
   
    listev2.append(v1)
    print(v1)
    time.sleep(60)

print(listev2)  

#3ème periode : 50 min
after = time.time()+3000
listev3 = []
url = 'https://www.boursorama.com/cours/1rPKER/'

while time.time()< after :
    
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'lxml')
   
    test = soup.find('span', {'class':'c-instrument c-instrument--last'})
    
#    print(test)
#valeur de l'action Kering
    v1 = test.text
    
   
    listev3.append(v1)
    print(v1)
    time.sleep(60)

print(listev3)


#Les trois listes de collecte de données 

listev1 = ['710.20', '710.30', '710.30', '710.60', '710.40', '710.00', '709.70', '709.50', '709.90', '709.60', '709.40', '709.60', '709.60', '709.90', '710.10', '709.90', '709.80', '709.90', '709.60', '709.30', '708.90', '708.30', '708.30', '708.10', '707.60', '707.60', '707.40', '706.90', '707.20', '707.50', '707.00', '707.30', '707.30', '707.60', '707.60', '707.90', '707.90', '707.70', '707.70', '707.60', '707.20', '706.10', '706.40', '706.50', '706.20', '706.50', '706.60', '706.50', '706.60', '706.60', '706.40', '706.50', '706.40', '705.70', '705.20', '705.00', '704.80', '705.00', '705.30', '705.50', '704.50', '704.40', '704.50', '704.30', '704.50', '704.50', '704.20', '704.30', '704.00', '703.50', '703.50', '703.10', '703.40', '703.30', '703.30', '703.00', '703.40', '703.10', '702.50', '701.80', '701.80', '702.50', '701.90', '702.30', '701.50', '701.30', '701.50', '701.40', '701.60', '701.90', '702.00', '702.10', '701.70', '701.40', '700.60', '700.40', '701.00', '702.10', '702.30']
print(listev1)

listev2=['704.00', '704.50', '703.30', '702.70', '702.70', '702.40', '702.90', '702.00', '702.90', '702.70', '702.60', '703.00', '703.50', '704.30', '703.50', '703.20', '704.20', '704.50', '703.80', '704.80', '705.70', '706.10', '707.20', '707.30', '708.10', '708.10', '708.80', '708.80', '709.40', '709.40', '709.40', '708.80', '708.70', '709.00', '708.80', '708.70', '708.60', '708.60', '708.10', '708.50', '708.60', '708.10', '708.90', '709.30', '709.30', '709.70', '710.10', '710.70', '710.70', '710.90']
print(listev2)

listev3=['710.80', '710.80', '710.90', '710.40', '710.40', '711.00', '710.90', '711.10', '711.10', '711.50', '711.50', '711.50', '711.30', '710.30', '710.00', '709.50', '709.20', '709.50', '709.70', '710.20', '710.20', '710.70', '711.50', '711.80', '712.30', '712.30', '712.00', '711.90', '711.90', '711.80', '710.90', '709.70', '710.10', '710.50', '710.50', '710.00', '710.10', '710.30', '710.10', '710.70', '710.60', '711.10', '710.90', '710.40', '710.60', '710.50', '710.80', '710.70', '710.70', '711.00']
print(listev3) 
#corriger les données : on a 99 données dans la première collecte et 50 dans les autres. On scinde donc en deux la liste v1 qui nous donne listev0 et listev11.  

listev11 = listev1[49:]
print(listev11)
listev0 = listev1[:50]
print(listev0)
#les quatre listes de données
listev0 = ['710.20', '710.30', '710.30', '710.60', '710.40', '710.00', '709.70', '709.50', '709.90', '709.60', '709.40', '709.60', '709.60', '709.90', '710.10', '709.90', '709.80', '709.90', '709.60', '709.30', '708.90', '708.30', '708.30', '708.10', '707.60', '707.60', '707.40', '706.90', '707.20', '707.50', '707.00', '707.30', '707.30', '707.60', '707.60', '707.90', '707.90', '707.70', '707.70', '707.60', '707.20', '706.10', '706.40', '706.50', '706.20', '706.50', '706.60', '706.50', '706.60', '706.60']
print(listev0)

listev11 = ['706.60', '706.40', '706.50', '706.40', '705.70', '705.20', '705.00', '704.80', '705.00', '705.30', '705.50', '704.50', '704.40', '704.50', '704.30', '704.50', '704.50', '704.20', '704.30', '704.00', '703.50', '703.50', '703.10', '703.40', '703.30', '703.30', '703.00', '703.40', '703.10', '702.50', '701.80', '701.80', '702.50', '701.90', '702.30', '701.50', '701.30', '701.50', '701.40', '701.60', '701.90', '702.00', '702.10', '701.70', '701.40', '700.60', '700.40', '701.00', '702.10', '702.30']
print(listev11)

listev2=['704.00', '704.50', '703.30', '702.70', '702.70', '702.40', '702.90', '702.00', '702.90', '702.70', '702.60', '703.00', '703.50', '704.30', '703.50', '703.20', '704.20', '704.50', '703.80', '704.80', '705.70', '706.10', '707.20', '707.30', '708.10', '708.10', '708.80', '708.80', '709.40', '709.40', '709.40', '708.80', '708.70', '709.00', '708.80', '708.70', '708.60', '708.60', '708.10', '708.50', '708.60', '708.10', '708.90', '709.30', '709.30', '709.70', '710.10', '710.70', '710.70', '710.90']
print(listev2)

listev3=['710.80', '710.80', '710.90', '710.40', '710.40', '711.00', '710.90', '711.10', '711.10', '711.50', '711.50', '711.50', '711.30', '710.30', '710.00', '709.50', '709.20', '709.50', '709.70', '710.20', '710.20', '710.70', '711.50', '711.80', '712.30', '712.30', '712.00', '711.90', '711.90', '711.80', '710.90', '709.70', '710.10', '710.50', '710.50', '710.00', '710.10', '710.30', '710.10', '710.70', '710.60', '711.10', '710.90', '710.40', '710.60', '710.50', '710.80', '710.70', '710.70', '711.00']
print(listev3) 

#Corriger les valeurs manquantes : 
#On a la liste v0 avec 49 données au lieu de cinquente. On considère cette valeur manquante comme independante de la variable du cours boursier qui nous intéresse. La probabilité d'absence est la même pour toutes les données et ne depends pas de parametres exterieurs mais de la façon dont nous avons decoupe le temps. 
#C'est donc un Missing Completely At Random (MCAR). Pour corriger cela, on utilise la méthode des plus proches voisins pour proceder a l'imputation. 
#On a donc une nouvelle liste v0 : 
listev0= ['710.20','710.25', '710.30', '710.30', '710.60', '710.40', '710.00', '709.70', '709.50', '709.90', '709.60', '709.40', '709.60', '709.60', '709.90', '710.10', '709.90', '709.80', '709.90', '709.60', '709.30', '708.90', '708.30', '708.30', '708.10', '707.60', '707.60', '707.40', '706.90', '707.20', '707.50', '707.00', '707.30', '707.30', '707.60', '707.60', '707.90', '707.90', '707.70', '707.70', '707.60', '707.20', '706.10', '706.40', '706.50', '706.20', '706.50', '706.60', '706.50', '706.60']
print(listev0)

###Dataframes
#On veut des listes de valeurs numeriques
listev0 = list(map(float, listev0))
listev11 = list(map(float, listev11))
listev2 = list(map(float, listev2))
listev3 = list(map(float, listev3))

 

import pandas as pd 
import matplotlib.pyplot as plt

#constitution des dataframes
d = {'Période 1':listev0, 'Période 2':listev11, 'Période 3':listev2, 'Période 4':listev3}
df = pd.DataFrame(d, columns=['Période 1', 'Période 2', 'Période 3', 'Période 4'])
print(df)
df=df.transpose(copy=False)
print(df)
###Analyse, modele et resultat

#Visualisation des données
plt.scatter('Période 1', 'Période 2', data=df)
plt.xlabel('Période 1')
plt.ylabel('Période 2')
plt.show()

#Modele de regression lineaire simple
from sklearn import linear_model


reg = linear_model.LinearRegression()

#créer y et X
#selection de la première colonne de notre dataset (la période 1)
X = df.iloc[0:len(df),0]
#selection de deuxième colonnes de notre dataset (la période 2)
Y = df.iloc[0:len(df),1]

#Visualisation des données
axes = plt.axes()
axes.grid() # dessiner une grille pour une meilleur lisibilité du graphe
plt.scatter(X,Y) # X et Y sont les variables qu'on a extraite dans le paragraphe précédent
plt.xlabel('Période 1')
plt.ylabel('Période 2')
plt.show()
#Modèle
from scipy import stats
#linregress() renvoie plusieurs variables de retour. On s'interessera 
# particulierement au slope et intercept
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
print(slope, intercept, r_value, p_value, std_err)

##resultats
#LinregressResult(slope=1.067230104499859, intercept=-52.686604337386484, 
#rvalue=0.8983176568157031, pvalue=9.084890105750394e-19, stderr=0.07533811142151199, 
#intercept_stderr=53.36939570376887)

####Commentaire sur le modèle : la fonction F(Période 1) = slope*Période 1 +Intercept vérifie y = Période 2, d'où y = f(x). 

##Entrainer le modèle
def predict(x):
   return slope * x + intercept
#la variable fitLine sera un tableau de valeurs prédites depuis la tableau de variables X
fitLine = predict(X)
plt.plot(X, fitLine, c='r')

#exemple avec la ligne 44, on devrait avoir Y = 701.4
print (predict(706.5))
#on a 701.31146

##On refait de même avec Période 2 et 3
X = df.iloc[0:len(df),1]
#selection de deuxième colonnes de notre dataset (la période 2)
Y = df.iloc[0:len(df),2]

#Visualisation des données
axes = plt.axes()
axes.grid() # dessiner une grille pour une meilleur lisibilité du graphe
plt.scatter(X,Y) # X et Y sont les variables qu'on a extraite dans le paragraphe précédent
plt.xlabel('Période 2')
plt.ylabel('Période 3')
plt.show()
#Modèle
from scipy import stats
#linregress() renvoie plusieurs variables de retour. On s'interessera 
# particulierement au slope et intercept
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
print(slope, intercept, r_value, p_value, std_err)
#resultats : -1.509773399129442 1768.475983450105 -0.8873580446297454 9.331480546663336e-18 0.11323208345811511

##Commentaire : Le modèle est toujours efficients sur ces deux périodes, 
#mais donne un resultat opposé au premier modele. Conclusion : valeur prédictible sur un intervalle de temps de moins d'1h40,
#mais sur le plus long terme, les variations ne sont pas linéaires. 












































710.20
710.30
710.30
710.60
710.40
710.00
709.70
709.50
709.90
709.60
709.40
709.60
709.60
709.90
710.10
709.90
709.80
709.90
709.60
709.30
708.90
708.30
708.30
708.10
707.60
707.60
707.40
706.90
707.20
707.50
707.00
707.30
707.30
707.60
707.60
707.90
707.90
707.70
707.70
707.60
707.20
706.10
706.40
706.50
706.20
706.50
706.60
706.50
706.60
706.60
706.40
706.50
706.40
705.70
705.20
705.00
704.80
705.00
705.30
705.50
704.50
704.40
704.50
704.30
704.50
704.50
704.20
704.30
704.00
703.50
703.50
703.10
703.40
703.30
703.30
703.00
703.40
703.10
702.50
701.80
701.80
702.50
701.90
702.30
701.50
701.30
701.50
701.40
701.60
701.90
702.00
702.10
701.70
701.40
700.60
700.40