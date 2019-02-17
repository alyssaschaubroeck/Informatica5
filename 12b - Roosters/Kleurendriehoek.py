def volgende_rij(rij):
    volgende = []
    for i in range(len(rij) - 1):
        if rij[i] == rij[i + 1]:
            volgende.append(rij[i])
        elif rij[i] != rij[i + 1]:
            kleur = ['Y', 'R', 'G']
            kleur.remove(rij[i])
            kleur.remove(rij[i + 1])
            volgende.append(kleur[0])
    return volgende

def driehoek(rij):
    volledig = []
    i = 0
    volledig.append(rij)
    while len(volledig[i]) > 1:
        volgend = volgende_rij(volledig[i])
        volledig.append(volgend)
        i += 1
    return volledig

def kleuren(driehoek):
    groen = 0
    rood = 0
    geel = 0
    for i in range(len(driehoek)):
        for b in range(len(driehoek[i])):
            kleur = driehoek[i][b]
            if kleur == 'G':
                groen += 1
            elif kleur == 'R':
                rood += 1
            elif kleur == 'Y':
                geel += 1
    return (groen, rood, geel)

print(kleuren([['Y', 'R', 'G', 'Y', 'Y'], ['G', 'Y', 'R', 'Y'], ['R', 'G', 'G'], ['Y', 'G'], ['R']]))