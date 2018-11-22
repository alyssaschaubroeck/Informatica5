#def welkom(naam):
    #print('Welkom terug ' + naam)

#welkom('Lieve Sint')
#print(welkom('Kerstman'))
#dan print hij ... en none
#als in functie niet return staat, dan zegt hij none

#def discriminant(a, b, c):
    #return (b ** 2) - (4 * a * c)

#d = discriminant(2,4,2)
#print(d)

appel = 'appel'
banaan = 'banaan'
kers = 'kers'
#globale variabelen overal bekend tenzij in functie nieuwe veriable

def print_fruit():
    appel = 'olifant'
    banaan = 'aapje'
    kers = 'goudvis'
    print(appel, banaan, kers)
#alleen gekend in die functie
#lokale variabele alleen gekend in functie

print_fruit()
print(appel, banaan, kers)

#de functie ord = alle kleine letters en alle kleine letters volgen elkaar, tussen grote en kleine letters zitten nog andere dingen
#de functie chr(zonder string) = geeft een letter
#chr(ord(('M') + 10))
#zal 'W' geven

