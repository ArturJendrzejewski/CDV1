#pi
import math
pi=math.pi
print(pi)

#pierwiastek
x=math.sqrt(9)
print(x)

#Losowanie
import random
rand=random.random()
print(rand)

list=random.choice([1,2,3,4,5,6])
print(list)


lista=random.choice([1,2,3,4,5,6,7,8,9,10])
print(lista)
liczba=input("podaj liczbę =")
if int(liczba)==int(lista):
    print("wygrales")
else:
    print("przegrales")
