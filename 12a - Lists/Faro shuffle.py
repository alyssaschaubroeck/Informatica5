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
    midden = lengte // 2
    eerste = lijst[:midden]
    tweede = lijst[midden:]
    return eerste, tweede

def faro_shuffle(lijst_1, lijst_2):
    i, b = 0, 0
    antw = []
    while i in range(len(lijst_1)) and b in range(len(lijst_2)):
        antw.append(lijst_1[i])
        antw.append(lijst_2[b])
        i += 1
        b += 1
    if len(lijst_1) < len(lijst_2):
        antw.append(lijst_2[b])
    return antw

print(faro_shuffle(['dood 0', 'dood 1', 'liefde 0'],['liefde 1', 'tijd 0', 'tijd 1']))