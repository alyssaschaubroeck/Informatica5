def versleutel_woord(woord, cijfer):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    nieuw_woord = ''
    rotatie = ''
    for i in range(0, len(woord)):
        if woord[i] in alfabet:
            nieuw_woord += woord[i].upper()
        elif woord[i] not in alfabet:
            nieuw_woord += woord[i]
    for i in range(0, len(nieuw_woord)):
        rotatie += chr(ord(nieuw_woord[i]) + cijfer)
    for i in range(0, len(rotatie)):
        rotatie = rotatie.replace('@', ' ')
    return rotatie

def versleutel_zin(zin, cijfer):
    woord = ''
    antw = ''
    eind = zin.find(' ')
    while zin[-1] != '.':
        woord += zin[:eind-1]
        zin = zin[eind+1:]
        antw += versleutel_woord(woord,cijfer)
        antw += '@'
        eind = zin.find(' ')
    return antw

print(versleutel_zin('De VS is al enkele weken in de ban van het datalek van Equifax.', 1))
