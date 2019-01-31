def versleutel_woord(woord, n):
#tekst bijschrijven voor werkwijze
    code = ''

    woord = woord.upper()

    for letter in woord:

        code_letter = chr(ord(letter) + n)

        if code == '@':
            code_letter = ' '

        code += code_letter

    return code

def versleutel_zin(zin, getal):

    index_spatie = zin.find(' ')
    code = ''

    while index_spatie != -1:
        woord = zin[:index_spatie]
        zin = zin[index_spatie + 1:]

        code += '@' + versleutel_woord(woord, getal)
        index_spatie = zin.find(' ')

    if len(zin) > 0:
        code += '@' + versleutel_woord(zin,getal)

    return code
