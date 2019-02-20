def kleur_toevoegen(verwerkt, kleur):
    if kleur == 'rood':
        verwerkt[0] += 1
    elif kleur == 'groen':
        verwerkt[1] += 1
    elif kleur == 'blauw':
        verwerkt[2] += 1
    return verwerkt

def is_wit(lijst):
    if lijst[0] == lijst[1] == lijst[2]:
        antw = True
    else:
        antw = False
    return antw

def verf_verzamelen(kleuren):
    begin = [0, 0, 0]
    begin = kleur_toevoegen(begin, kleuren[0])
    i = 1
    while is_wit(begin) is False and i in range(len(kleuren)):
        begin = kleur_toevoegen(begin, kleuren[i])
        i += 1
    if is_wit(begin) is True:
        return i, begin
    elif is_wit(begin) is False:
        return None

print(verf_verzamelen(['blauw', 'rood', 'groen', 'blauw', 'groen', 'rood', 'blauw', 'rood', 'blauw', 'rood', 'rood', 'blauw', 'blauw', 'rood', 'groen', 'rood', 'groen']))
