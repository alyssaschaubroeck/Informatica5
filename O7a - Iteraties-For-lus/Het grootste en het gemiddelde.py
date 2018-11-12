#input
aantal = int(input('aantal getallen: '))
max = 0
som = 0

#input getallen
for i in range(aantal):
    getal = int(input('getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    som += getal

#bewerking
gemiddelde = som / aantal

print('Het grootste getal is {:d} en het gemiddelde is {:.2f}'. format(max, gemiddelde))