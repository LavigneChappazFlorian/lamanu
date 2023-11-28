def exo1():
    user_number = input("Donner un chiffre : ")
    user_number = int(user_number)
    while not(1 <= user_number <= 3):
        user_number = input("Donner un nouveau chiffre : ")
        user_number = int(user_number) 
   

def exo2():
    number = int(input("Donner un chiffre entre 10 et20 "))
    
    while not (20 >= number >= 10):
        if number < 10:
            number=int(input("Plus grand : " ))
        if number > 20:
            number=int(input("Plus petit : "))
    
    print("GG =)")

def exo3():

    user_number = int(input("Entrez un nombre : "))
    print("For")
    for number in range (user_number + 1, user_number +11):
        print(number)
    
    print("While")
    count = 0
    while count < 10 :
        print(user_number + count + 1)
        count += 1

def exo4():
    sum = 0
    user_number = int(input("Entrer un nombre à ajouter :"))
    while user_number != 0:
        sum += user_number
        user_number = int(input("Entrer un nombre à ajouter :"))
    
    print(f"Somme {sum}")

        

def exo5():
    list = []
    user_number = int(input("mettre un nombre entier :"))
    
    while user_number != 0 :
        list.append(user_number)
        user_number = int(input("ajouter un nombre entier :"))


    print(sum(list))

def exo6():
    languages = [
        "Python",
        "Javascript",
        "Java",
        "C++",
        "Cobol"
    ]

    for language in languages : 
        print(language)

    for i in range(0, len(languages)):
        print(languages[i])

    index = 0 
    while index < len(languages)  :
        print(languages[index])
        index += 1
    
def exo7():
    list = []
    for i in range(3):
        nombre = int(input("Entrer un nombre : "))
        list.append(nombre)

    maxi = max(list)
    # maxi = list[0]
    # for i in list:
    #     if i > maxi:
    #         maxi = i
    
    print("Le nombre le plus grand est", maxi)


    
    





    

def exo8():
    list = []
    for i in range(3):
        nombre = int(input("Entrer un nombre : "))
        list.append(nombre)

    #maxi = max(list)
    #position = list.index(maxi) +1
    maxi = list[0]
    position = 0
    for i in range(len(list)):
        if list[i] > maxi:
            maxi = list[i]
            position = i + 1
    
    print("Le nombre le plus grand est", maxi, "en position", position)

exo8()


# print random number between 1 and 12
# import random
# print(random.randint(1,12))

