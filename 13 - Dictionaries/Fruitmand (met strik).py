def fruitmand_maken(lijst):
    fruitmand = {}
    for item in lijst:
        if len(item) not in fruitmand.keys():
            fruitmand[len(item)] = item
        else:
            oud = fruitmand[len(item)]
            if lijst.count(item) >= lijst.count(oud):
                fruitmand.pop(len(item))
                fruitmand[len(item)] = item
    return fruitmand

def fruitmand_inpakken(fruitmand):
    fruit = []
    while len(fruitmand) != 0:
        laagste = min(fruitmand.keys())
        fruit.append(fruitmand[laagste])
        fruitmand.pop(laagste)
    return fruit

print(fruitmand_inpakken({6: 'banaan', 7: 'aardbei', 4: 'peer', 5: 'appel', 3: 'bes', 11: 'sinaasappel', 8: 'framboos'}))
