def fruitstuk_toevoegen(fruitmand, fruit):
    for item in fruitmand:
        if len(item) == len(fruit):
            fruitmand.remove(item)
    fruitmand.append(fruit)
    fruitmand.sort(key = len)
    return fruitmand

def maak_fruitmand(lijst):
    i = 0
    while i in range(len(lijst) - 2):
        if len(lijst[i]) == len(lijst[i + 1]):
            eerst = lijst.count(lijst[i])
            tweede = lijst.count(lijst[i + 1])
            if eerst > tweede:
                lijst.remove(lijst[i + 1])
                lijst.append(lijst[i])
            else:
                lijst.remove(lijst[i])
                lijst.append(lijst[i + 1])
        i += 1
    for item in lijst:
        while lijst.count(item) > 1:
            lijst.remove(item)
    lijst.sort(key = len)
    return lijst

print(maak_fruitmand(['kiwi', 'peer', 'kiwi', 'peer', 'kiwi']))