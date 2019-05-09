kaart = {'Brugge': {'Gent', 'Antwerpen'}, 'Kortrijk': {'Gent'}, 'Gent': {'Antwerpen', 'Kortrijk', 'Brugge'},
         'Antwerpen': {'Gent', 'Brussel', 'Brugge'}, 'Brussel': {'Hasselt', 'Antwerpen'}, 'Hasselt': {'Brussel'}}

def bestaat_weg(stad1, stad2, kaart):
    lijst = kaart.get(stad1)
    antwoord = {stad2}.isdisjoint(lijst)
    return not antwoord

def geen_dubbelburen(stad1, stad2, kaart):
    #alle verbindingen
    lijst1, lijst2 = kaart.get(stad1), kaart.get(stad2)

    #steden die 1 keer voorkomen
    antwoord1, antwoord2 = lijst1.difference(lijst2), lijst2.difference(lijst1)

    #steden samenvoegen
    antwoord = antwoord1.union(antwoord2)

    #de oorspronkelijke stad weghalen
    antwoord.discard(stad1)
    antwoord.discard(stad2)
    return antwoord

def bereikbaarheid_meest_afgelegen_stad(kaart):
    aantal = []
    for key in kaart:
        aantal += str(len(kaart.get(key)))
    return int(min(aantal))

def bestaat_route(steden, kaart):
    antwoord, i = True, 0
    while bestaat_weg(steden[i], steden[i + 1], kaart) is True and i in range(len(steden)- 2):
        antwoord = True
        i += 1
    if bestaat_weg(steden[i], steden[i + 1], kaart) is False:
        antwoord = False
    return antwoord

print(bestaat_route(['Hasselt', 'Brussel', 'Antwerpen', 'Brugge', 'Gent', 'Kortrijk'], kaart))