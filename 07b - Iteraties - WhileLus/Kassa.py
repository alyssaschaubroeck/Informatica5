prijs = 1
beginprijs = 0

while prijs > 0:
    prijs = float(input('Prijs:'))
    beginprijs += prijs

print('De totale prijs is €', '{:.2f}'.format(beginprijs))