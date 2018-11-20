kaart = int(input('Kaart is: '))
totaal = 0

while totaal < 21 and kaart > 0:
    totaal += kaart
    if totaal < 21:
        kaart = int(input('Kaart is: '))

if kaart == 0:
    antw = 'Voorzichtig gespeeld ({})'.format(totaal)

if totaal == 21:
    antw = 'Gewonnen!'

if totaal > 21:
    antw = 'Verbrand ({})'.format(totaal)

print(antw)