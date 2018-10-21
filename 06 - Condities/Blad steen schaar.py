antwoord_1 = input('Persoon 1: ')
antwoord_2 = input('Persoon 2: ')

if antwoord_1 == antwoord_2:
    print('onbeslist')
elif antwoord_1 == 'blad' and antwoord_2 == 'steen':
    print('speler 1 wint')
elif antwoord_1 == 'steen' and antwoord_2 == 'schaar':
    print('speler 1 wint')
elif antwoord_1 == 'schaar' and antwoord_2 == 'blad':
    print('speler 1 wint')
else:
    print('speler 2 wint')


