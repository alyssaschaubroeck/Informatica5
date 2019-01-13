def hint(gok, woord):
    antw = ''
    for i in range(0, 4):
        if i not in woord:
            antw = '.....'
        elif gok.find([i]) == woord.find([i]):            antw += antw.upper([i])
        elif gok[i] in woord[:]:
            antw += i

    return antw

print(hint('spoed','depri'))




