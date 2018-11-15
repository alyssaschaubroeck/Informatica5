#getal = 0
#while getal < 5:
    #print(getal)
    #getal += 1

#for i in range(+0, 5):
    #print(i)

from random import randint
temp = randint(-10, 3)
vorst_periode = 0

while temp < 0:
    vorst_periode += 1
    temp = randint(-10, 30)

print(vorst_periode, 'dagen')

#computer zelf bereken, op voorhand weet je niet hoelang het gaat duren
# gemakkelijk een oneindige lus programeren
