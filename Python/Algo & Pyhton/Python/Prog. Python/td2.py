 # TD2 exo 1
age=int(input("quel est ton age ?" ))
age= age*age
print (age)


#TD2 exo 2
article_price_htc=int(input("Quel est le prix de ton article ?  "))
quantite_article=int(input("Quelle quantité veux tu ?  "))
TVA_rate = int(input(float()))
TVA_rate /= 100
article_price_ttc = article_price_htc * (1+ TVA_rate)

print()
print("Le prix TTC de votre panier est de", article_price_ttc * quantite_article, "€")
