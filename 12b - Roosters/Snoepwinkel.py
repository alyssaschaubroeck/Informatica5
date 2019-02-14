from operator import itemgetter

def bereken_prijs(artikelen):
    prijs = 0
    for item in artikelen:
        prijs += item[1]
    return prijs

def winkelbriefje(lijst):
    artikelen = []
    for item in lijst:
        artikelen.append(item[0])
    return artikelen

def sorteer(lijst):
    lijst.sort(key=itemgetter(1))
    return lijst

print(sorteer([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))