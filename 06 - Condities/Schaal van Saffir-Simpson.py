antwoord = int(input('Wat is de windsnelheid? '))

if antwoord < 119:
    print('geen orkaan')
elif antwoord >= 210 and antwoord <= 249:
    print('categorie 4')
elif antwoord >= 178 and antwoord <= 209:
    print('categorie 3')
elif antwoord >= 154 and antwoord <= 177:
    print('categorie 2')
elif antwoord >= 119 and antwoord <= 153:
    print('categorie 1')
else:
    print('categorie 5')
