def geldige_zet(schaakzet):
    # antw = false dan else niet nodig
    if len(schaakzet) == 3 and schaakzet[0] in 'KDTLP' and schaakzet[1] in 'abcdefgh' and schaakzet[2] in '123456789':
        antw = True
    elif len(schaakzet) == 2 and schaakzet [0] in 'abcdefgh' and schaakzet[1] in '123456789':
        antw = True
    else:
        antw = False
    return antw

def geldige_zetten(schaakzetten):
    antw = True
    i = 0
    #while i < len(schaakzetten) and geldige_zet(schaakzetten[i])
        #i += 1
    #return i >= len(schaakzetten)
    while antw == True and i in range(0, len(schaakzetten) - 1):
        nieuw = schaakzetten[i]
        antw = geldige_zet(nieuw)
        i += 1
    return antw

print( geldige_zetten(('Ta1', 'e5', 'h8', 'f7', 'Db7', 'Lg3')))