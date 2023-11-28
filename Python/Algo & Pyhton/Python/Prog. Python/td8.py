#Exo 1

""" classification_dewey = ("Généralités","Philosophie","Religion","Sciences Sociales","Langues","Sciences","Technologies","Arts, loisirs et sports","Littérature","Histoire - Géographie")

reference = input("Entrez la référence de votre livre : ")

while reference != "stop" :

    if len(reference) != 3 or int(reference) > 900 :
        print("Veuillez saisir une référence valide à 3 chiffres s'il vous plaît")
        reference =input("Entrez la référence de votre livre : ")

    else : 
        
        if "000" <= reference < "100" :
            print("La référence de votre livre est", classification_dewey[0])
            reference =input("Entrez la référence de votre livre : ")

        if "100" <= reference < "200" :
            print("Voici la référence de votre livre :", classification_dewey[1])
            reference =input("Entrez la référence de votre livre : ")

        if "200" <= reference < "300" :
            print("Voici la référence de votre livre :", classification_dewey[2])
            reference =input("Entrez la référence de votre livre : ")

        if "300" <= reference < "400" :
            print("Voici la référence de votre livre :", classification_dewey[3])
            reference =input("Entrez la référence de votre livre : ")

        if "400" <= reference < "500" :
            print("Voici la référence de votre livre :", classification_dewey[4])
            reference =input("Entrez la référence de votre livre : ")

        if "500" <= reference < "600" :
            print("Voici la référence de votre livre :", classification_dewey[5])
            reference =input("Entrez la référence de votre livre : ")

        if "600" <= reference < "700" :
            print("Voici la référence de votre livre :", classification_dewey[6])
            reference =input("Entrez la référence de votre livre : ")

        if "700" <= reference < "800" :
            print("Voici la référence de votre livre :", classification_dewey[7])
            reference =input("Entrez la référence de votre livre : ")

        if "800" <= reference < "900" :
            print("Voici la référence de votre livre :", classification_dewey[8])
            reference =input("Entrez la référence de votre livre : ")

        if "900" <= reference < "999" :
            print("Voici la référence de votre livre :", classification_dewey[9])
            reference =input("Entrez la référence de votre livre : ") """



#Exo 2

import json

classification_dewey = ("Généralités","Philosophie","Religion","Sciences Sociales","Langues","Sciences","Technologies","Arts, loisirs et sports","Littérature","Histoire - Géographie")

#Liste des livres
books = []

#Dictionnaire des livres
book = {}

#Continuer à remplir la liste
choice = input("Voulez vous ajouter un nouveau livre ? oui/non : ")

#Boucle infini pour ajouter un livre
while choice != "non" :

    if choice == "oui" :
        book["Titre"] = input("Le titre du livre : ")
        book["Auteur"] = input("L'auteur du livre : ")
        book["Exemplaires"] = input("Le nombre d'exemplaires du livre : ")
        book["Genre"] = input("Le genre du livre : ")
        books.append(book)

        choice = input("Voulez vous ajouter un nouveau livre ? oui/non : ")

    else : 
        exit()

with open("top_books_2021.json", "w") as file:
    json.dump(books, file)

f = open("top_books_2021.json")
data = json.load(f)







