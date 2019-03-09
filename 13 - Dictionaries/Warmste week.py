def gift_inschrijven(klas, totaal):
    if klas[0] in totaal:
        totaal[klas[0]] += klas[1]
    else:
        totaal[klas[0]] = klas[1]
    return totaal

print(gift_inschrijven(('5IN', 73.81),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 232.48}))