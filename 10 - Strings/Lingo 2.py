def hint(gok, woord):
    antw = gok
    for i in range(0,5):
        if gok[i] not in woord:
            antw = antw.replace(gok[i], '.')
        elif gok[i] in woord:
            if gok.find('[i]') == woord.find('[i]'):
                antw = antw.replace(gok[i], gok[i].upper())
            else:
                antw = antw.replace(gok[i], gok[i].lower())
    return antw

print(hint('spoed', 'depri'))