#Florian Lavigne

#Exercice 1 

# Question 1 
number_list = []
for i in range(10) :
    i = int(input("Ecriver ici un nombre entre 0 et 10 :"))
    number_list.append(i)
print("La somme des entiers de la liste est", sum(number_list)) 

#Question 2

#Question 3
number_list = [0 , 1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
number_list.reverse()
print(number_list)

#Exercice 2 

#Question 1

# Pour l[-2], on obient [5]
l=[1,5,10] 
print(l[-2])

# Pour l[-2 :], on obient [5, 10]
l=[1,5,10] 
print(l[-2 :])

#Question 2

numbers = [8,6,4,49,8,2,16]
print(numbers[-3 :])

