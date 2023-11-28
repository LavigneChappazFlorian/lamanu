# exo1 
#number = int(input("Donner un chiffre 1 et 3 : "))
#while not 1 <= number <= 3:
    #number = int(input("Resaisissez une valeur svp : "))

# exo 2 
#number = int(input("Donner un chiffre 10 et 20 : "))
#while number < 10:
    #print("Plus grand !") 
    #number = int(input("Resaisissez une valeur svp : "))
#while number > 20 :
    #print("Plus petit !") 
    #number = int(input("Resaisissez une valeur svp : "))

# exo 3
#x = int(input("Donner un nombre svp : "))
#for i in range(x, x+11) :
    #print(i)

# exo 4 
#x = int(input("Donner un nombre svp : "))
#z = 0
#z = z + x
#while z > 0 :
    #x = int(input("Donner un nombre svp : "))
    #z = z + x
    #print(z)
    #if x == 0 :
        #exit()
    
#exo 5
#l#ist = []
#number = int(input("Ecriver un nombre : "))

#while number !=0 :
    #list.append(number)
    #number = int(input("Ajouter un nombre entier : "))

#print("La somme totale des nombres de la liste est de :", sum(list))


def exo6():

list = ["Python", "Javascript", "Java", "PHP", "C++", "Cobol"]
for langage in list:
    print(langage)

i = 0
while i < len(list):
  print(list[i])
  i = i + 1


def exo7():

list = []

for i in range(20):
	number = int(input("Entrer un nombre : "))
	list.append(number) #permet d'ajouter un élément

print("Le plus grand nombre est", max(list))



def exo8(): 
      
list = []
for i in range(20):
	number = int(input("Entrer un nombre : "))
	list.append(number) #permet d'ajouter un élément
	cible = number #Permet de déterminer le nombre pour lequel on a besoin de sa position

print("Le plus petit nombre est", min(list), "en position", list.index(cible))

exo8()
