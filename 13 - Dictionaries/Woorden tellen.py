def woord_frequentie(zin):
    uitkomst = {}
    zin = zin.lower()
    zin = zin.replace('.', ' ')
    zin = zin.split()
    for item in zin:
        if item not in uitkomst:
            aantal = zin.count(item)
            uitkomst[item] = aantal
    return uitkomst

def woorden_per_frequentie(zin):
    uitkomst = {}
    aantal_keer = woord_frequentie(zin)
    for key, value in aantal_keer.items():
        if value not in uitkomst:
            uitkomst[value] = [key]
        else:
            uitkomst[value].append(key)
    return uitkomst

def meest_gebruikte_woorden(zin):
    frequentie = woorden_per_frequentie(zin)
    grootst = max(frequentie.keys())
    uitkomst = frequentie.get(grootst)
    return uitkomst

print(meest_gebruikte_woorden('Dit is een zin. En nog een zin. En een laatste zin.'))