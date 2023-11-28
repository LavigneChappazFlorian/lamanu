#TD4 exo 1
hours = int(input("Ecriver une heure ici : "))
minutes = int(input("Ecriver la ou les minutes ici : "))
secondes= int(input("Ecriver les secondes ici : "))
secondes = secondes + 1
if secondes == 60 :
    secondes = 00
    minutes = minutes + 1
if minutes == 60 :
    minutes = 00
    hours = hours + 1
if hours == 24 :
    hours = 00
print("Dans une seconde, il sera ",hours, "heure(s)",minutes,"minute(s)",secondes, "seconde(s)")

#TD4 exo 3
photo= int(input("Combien de photocopies voulez-vous ?"))
total=0
if photo<=10:
    total=photo*0.10
elif 10<photo<=20:
    total=10*0.10
    photorestantes = photo-10
    total= total+photo*0.09

else:
    total=10*0.10
    photorestantes= photo-10
    total=total+20*0.09
    photorestantes= photo-20
    total=total+photorestantes*0.08

print("Votre facture pour les photocopies est de" ,total, "€.")

#TD4 exo 4
#EXERCICE 4

def exo4() :

    candidat1 = input("Score Candidat 1 : ")
    candidat2 = input("Score Candidat 2 : ")
    candidat3 = input("Score Candidat 3 : ")
    candidat4 = input("Score Candidat 4 : ")

    candidat1 = float(candidat1)
    candidat2 = float(candidat2)
    candidat3 = float(candidat3)
    candidat4 = float(candidat4)

    if (candidat1 + candidat2 + candidat3 + candidat4) >= 100.0 :
        print("Erreur : La somme des valeurs est supérieure à 100")
        # exit(1)
    else:
        if candidat1 > 50.0 :
            print ("Le candidat 1 est élu.")
        elif candidat1 >= 12.5 and candidat1 < 50.0 and candidat1 > candidat2 > candidat3 > candidat4 :
            print ("Le candidat est en ballotage favorable")
        elif candidat1 >= 12.5 and candidat1 < 50.0 and not(candidat1 > candidat2 > candidat3 > candidat4):
            print ("Le candidat se trouve en ballotage défavorable")
        elif candidat1 < 12.5 :
            print ("Le candidat est battu.")



#TD4 exo 5 

    jour = input("Jour : ")
    mois = input("Mois : ")
    annee = input("Année : ")

    jour = int(jour)
    mois = int(mois)
    annee = int(annee)

    is_bis = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0

    if (
        (1900 <= annee <= 2050)
        and
        1 <= mois <= 12
        and
        ( mois in [1, 3, 5, 7, 8, 10, 12] and 1 <= jour <= 31)
        and
        (mois not in [1, 3, 5, 7, 8, 10, 12] and 1 <= jour <= 30)
        and
        # On ne veut pas de 29 février lors d'une année non bissextile
        not(mois == 2 and jour > 28 and not(is_bis))
        and
        # On ne veut pas de 30 février même lors d'une année bissextile
        not(mois == 2 and jour > 29 and is_bis)
    ):
        print("La date est valide.")
    else:
        print("La date est invalide")
        exit(1)