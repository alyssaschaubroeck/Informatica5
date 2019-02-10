def nieuw_kaartspel(kleuren, waarden):
    antw = []
    i = 0
    b = 0
    while i in range(len(kleuren)):
        while b in range(len(waarden)):
            antw.append(kleuren[i] + waarden[b])
            b += 1
        i += 1
        b = 0
    return antw

def splits_kaartspel(lijst):
    lengte = len(lijst)
    helft = lengte // 2
    eerstehelft = []
    i = 0
    while i in range(len(helft)):
        eerstehelft.append(lijst[i])
        i +=1


print(nieuw_kaartspel(['James '],['7']))