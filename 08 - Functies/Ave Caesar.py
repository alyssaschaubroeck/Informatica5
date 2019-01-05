#input
alfabet = 'abcdefghijklmnopqrstuvwxyz'
h_alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#letter of niet?
def is_letter(n):
    if n in alfabet or h_alfabet:
        letter = True
    else:
        letter = False
    return letter

#roteer letter
def roteer_letter(a, b):
    if letter in woord
    if is_letter(a) == True:
        rotatie = chr(ord(a) + b)
        return rotatie

#versleutel
def versleutel(tekst, ceasarcijfer):
    antwoord = roteer_letter(tekst,ceasarcijfer)
    return antwoord