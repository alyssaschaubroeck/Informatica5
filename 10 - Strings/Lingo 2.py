def hint(gok, woord):
    antw = '.....'
    for i in range(0,5):
        if gok[i] not in woord:
            antw = '.....'
        elif gok[i] in woord:
            if gok.find('[i]') == woord.find('[i]'):
                antw = antw.replace(gok[i], gok.upper())
            else:
                antw = gok[i]

    return antw

print(hint('spoed', 'depri'))