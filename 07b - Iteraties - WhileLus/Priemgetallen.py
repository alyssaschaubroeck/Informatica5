priemgetal = int(input('Priemgetal: '))
deelbaar = 1
getal = 2

while getal < priemgetal:
    if (priemgetal % getal) == 0:
        antw = '{} is geen priemgetal'.format(priemgetal)
        deelbaar = 0
    getal += 1
if deelbaar and priemgetal != 1:
    antw = '{} is een priemgetal'.format(priemgetal)
elif priemgetal == 1:
    antw = '1 is geen priemgetal'

print(antw)