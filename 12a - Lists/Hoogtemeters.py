def hoogtemeters(hoogtes):
    antwoord = []
    i = 0
    while i < len(hoogtes) - 1:
        volgendgetal = hoogtes[i + 1]
        getal = volgendgetal - hoogtes[i]
        antwoord.append(getal)
        i += 1
    return antwoord

def dalen_en_stijgen(lijst):
    gedaald = 0
    gestegen = 0
    for item in lijst:
        if item > 0:
            gestegen += item
        if item < 0:
            gedaald += abs(item)
    return gedaald, gestegen

print(dalen_en_stijgen([-761, 286, -113, 649, -547]))