#input
volledig = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabet = 'abcdefghijklmnopqrstuvwxyz'
h_alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#letter of niet?
def is_letter(n):
    if n in volledig:
        letter = True
    else:
        letter = False
    return letter

#roteer letter
def roteer_letter(letter, cijfer):
    if letter in alfabet:
        if ord(letter) + cijfer > 122:
            rotatie = chr(ord(letter) + cijfer - 26)
        else:
            rotatie = chr(ord(letter) + cijfer)
    elif letter in h_alfabet:
        if ord(letter) + cijfer > 90:
            rotatie = chr(ord(letter) + cijfer - 26)
        else:
            rotatie = chr(ord(letter) + cijfer)
    return rotatie

#versleutel
def versleutel(tekst, cijfer):
    antwoord = ''
    for letter in tekst:
        if is_letter(letter) == True:
            antwoord += roteer_letter(letter, cijfer)
        if is_letter(letter) == False:
            antwoord += letter
    return antwoord