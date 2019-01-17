def hint(gok, woord):
    antw = ''
    for i in range(0,5):
        if gok[i] not in woord:
            antw += '.'
        elif gok[i] in woord:
            if gok[i] == woord[i]:
                antw += gok[i].upper()
            else:
                antw += gok[i].lower()
    return antw

print(hint('spoed', 'depri'))