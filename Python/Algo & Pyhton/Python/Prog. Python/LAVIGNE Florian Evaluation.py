#Florian Lavigne
#Exercie 1 : Mention

note = float(input("Donner une note : "))

if note < 0 or note > 20 :
    print("Note invalide")

elif note < 12 :
    print("Note :",note,"/20")

elif note >= 12 and note < 14 :
    print("Note :", note,"/20, Assez bien")

elif note >= 14 and note < 16 :
    print("Note :", note,"/20, Bien")

elif note >= 16 and note < 18 :
    print("Note :", note,"/20, Très bien")

elif note >= 18 and note < 20 :
    print("Note :", note,"/20, Excellent")

elif note == 20 :
    print("Note :", note,"/20, Parfait")


#Exercice 2 : Bonjour !

age = int(input("Quel âge avez-vous ? : "))
gender = str(input("Quel est votre genre ? (H, F ou I) : ")) #Permet de savoir le genre de la personne en fonction du caractère choisi (H = Homme, F = Femme et I = Indéfini)

if gender == "H" :
    print("Bonjour Monsieur !")
elif gender == "I" :
    print("Bonjour !")
elif gender == "F" and age < 18 :
    print("Bonjour Mademoiselle !")
elif gender == "F" and age >= 18 :
    print("Bonjour Madame !")