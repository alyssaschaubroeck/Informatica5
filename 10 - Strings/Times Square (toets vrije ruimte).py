def bereken_prijs(boodschap):

    # boodschap zonder prijs
    stop = boodschap.find('<')
    eind = boodschap.find('>')
    nieuw = boodschap[:stop]

    # aantal tekens
    aantal = stop

    # totale prijs
    prijs = float(boodschap[stop + 1: eind])
    totaalprijs = aantal * prijs

    return nieuw, totaalprijs

def toon_boodschappen(boodschappen):
    eind = boodschappen.find('>')
    antw = ''
    nieuwprijs = 0
    while eind < len(boodschappen)-1:
        eind = boodschappen.find('>')
        nieuw, totaalprijs = bereken_prijs(boodschappen)
        boodschappen = boodschappen[eind+1:]
        antw += '\n'
        antw += nieuw
        nieuwprijs += totaalprijs
    return '{}{}'.format(nieuwprijs, antw)

print(toon_boodschappen('I spent my last money on this billboard. Please give me a job.<2.68>Dear Emma, I love You more than words can say. Please wil you marry me?<2.42>I LOVE YOU AND WANT TO SPENT FOREVER WITH YOU. WILL YOU MARRY ME?<0.76>'))