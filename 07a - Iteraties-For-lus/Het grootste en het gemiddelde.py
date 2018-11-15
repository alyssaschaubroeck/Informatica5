#input
aantal = int(input('aantal getallen: '))

max = int(input('getal: '))
som = max

#input getallen
for i in range(aantal - 1):
    getal = int(input('getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    som += getal

#bewerking
gemiddelde = som / aantal

print('Het grootste getal is {} en het gemiddelde is {:.2f}'. format(max, gemiddelde))

#tussen door print(som), twee dingen bereken, in twee delen
#het moet telkens groter dan het grootste vorig getal
#het grootste wordt bijhouden
#eerste getal inlezen voor de lus, dan is het sowieso het grootste
#dan moet je een geral minder bereken in range dus aantal - 1

#bij het kleinste is het hetzelfde geval